import os
import re
from math import ceil
from _io import BytesIO
from typing import Union
from docx import Document
from call.models import Call
from datetime import datetime
from datetime import timedelta
from google.cloud import storage
from student.models import Student
from rest_framework.request import Request
from application.models import Application
from data.constants import Constants


CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
STORAGE_CLIENT = storage.Client.from_service_account_json(CREDENTIALS)


def set_variables(request: Request, student: Student) -> dict[str, Union[str, list]]:
    """
    Returns a dictionary where the keys are the uppercase strings that should be replaced on the
    forms and the values are the strings that will be used to replace those upper strings. It includes
    the personal information of the student, info of its coordinator, info about the destination
    university and/or information about the courses (this one is a list).
    """
    # Info student
    attributes = dict()
    for attribute in student._meta.get_fields():
        try:
            if 'contact' in attribute.name:  # It is the contact person info
                contact_person = getattr(student, attribute.name)
                for attr_contact in contact_person._meta.get_fields():
                    try:
                        name_attr = attr_contact.name.upper()
                        attributes[f'CONTACT_{name_attr}'] = getattr(contact_person, attr_contact.name)
                    except AttributeError:  # It is like a many-to-one relation
                        continue
            elif attribute.choices is not None:  # It is an enum
                display_method_name = f'get_{attribute.name}_display'
                attributes[attribute.name.upper()] = getattr(student, display_method_name)()
            else:
                value = getattr(student, attribute.name)
                if value is None:  # The value has not been set (like diseases)
                    value = 'No hay'
                attributes[attribute.name.upper()] = value
        except AttributeError:  # It is like a many-to-one relation
            continue

    # Info coordinator
    headquarter = student.get_headquarter_display()
    faculty = student.get_faculty_display()
    major = student.get_major_display()
    info_coordinator = Constants.INFO_FACULTIES[headquarter][faculty][major]
    attributes['NAME_COORD_UNAL'] = info_coordinator['Coordinador Curricular']
    attributes['PHONE_COORD_UNAL'] = info_coordinator['Teléfono Coordinador']
    attributes['EMAIL_COORD_UNAL'] = info_coordinator['Correo Coordinador']

    # Info destination university
    call = Call.objects.get(id=request.data['call'])
    attributes['DEST_INSTITUTION'] = call.university_id.name
    attributes['DEST_COUNTRY'] = call.university_id.country
    attributes['DEST_CITY'] = call.university_id.city
    info_mobility = request.data.get('info_mobility')
    if info_mobility is not None:
        for name, info in info_mobility.items():
            if 'date' in name:
                info = datetime.strptime(info, '%d-%m-%Y')
            attributes[f'{name.upper()}'] = info
    if 'START_DATE' and 'END_DATE' in attributes:
        attributes['DURATION'] = ceil((attributes['END_DATE'] - attributes['START_DATE']).days / 30)
    if 'START_DATE' in attributes:
        attributes['START_DATE'] = attributes['START_DATE'].strftime('%d-%m-%Y')
    if 'END_DATE' in attributes:
        attributes['END_DATE'] = attributes['END_DATE'].strftime('%d-%m-%Y')

    # Info courses
    info_courses = request.data.get('info_courses')
    if info_courses is not None:
        attributes['INFO_COURSES'] = []
        for course in info_courses:
            info_course = {}
            for name, info in course.items():
                info_course[f'{name.upper()}'] = info
            attributes['INFO_COURSES'].append(info_course)

    # TODO: add date to forms (should it be UTF?)

    return attributes


def fill_forms(attributes: dict[str, str], path_original_forms: str, path_save_forms: str) -> None:
    """
    Replaces the keys of the given dictionary with the values of that dictionary in each form and
    saves them to the given path.
    """
    if not os.path.exists(path_save_forms):
        os.mkdir(path_save_forms)

    for name_form in os.listdir(path_original_forms):
        path_doc = os.path.join(path_original_forms, name_form)
        doc = Document(path_doc)

        # TODO: make filling of courses dynamic (does not depend on # of courses)
        # TODO: fix keep the original format
        # TODO: make it more efficient
        # TODO: finish filling up the forms with the uppercase words
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text in attributes:
                        pattern = r'\b{}\b'.format(re.escape(cell.text))
                        cell.text = re.sub(pattern, f'{attributes[cell.text]}', cell.text)

        for paragraph in doc.paragraphs:
            for word in paragraph.text.split():
                if word in attributes:
                    pattern = r'\b{}\b'.format(re.escape(word))
                    paragraph.text = re.sub(pattern, f'{attributes[word]}', paragraph.text)

        name, extension = name_form.split('.')
        new_name = f'{name}_{os.path.basename(path_save_forms)}.{extension}'
        doc.save(os.path.join(path_save_forms, new_name))


def upload_forms(path_save_forms: str) -> None:
    """
    Uploads the forms of the student and call to GCP, and them removes those forms and the
    folder.
    """
    bucket = STORAGE_CLIENT.bucket('filled_doc')

    list_forms = []
    for form in os.listdir(path_save_forms):
        blob = bucket.blob(form)
        path_form = os.path.join(path_save_forms, form)
        blob.upload_from_filename(path_form)
        list_forms.append(path_form)

    for form in list_forms:
        os.remove(form)
    os.rmdir(path_save_forms)


def get_link_file(type_file: str, file_name: str) -> str:
    """
    Return a public link to an object in a bucket that can be used from 10 minutes. If the file
    does not exist, a FileNotFoundError is raised. No need to send the extension of the file in
    its name.
    """
    bucket = STORAGE_CLIENT.bucket(type_file)
    blobs = bucket.list_blobs(prefix=file_name)
    try:
        blob = next(blobs)
    except StopIteration:
        raise FileNotFoundError

    # Set the expiration time for the signed URL
    url_expiration = timedelta(minutes=10)
    signed_url = blob.generate_signed_url(expiration=url_expiration, method='GET')

    return signed_url


def upload_object(name_bucket: str, source_file: BytesIO, destination_blob_name: str) -> None:
    """
    Uploads a file-like object to a bucket
    """
    bucket = STORAGE_CLIENT.bucket(name_bucket)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(source_file)


def check_docs(student: Student, call: Call) -> tuple[bool, list[str]]:
    """
    Used to make sure all the documents (depending on the region of the call) have been uploaded.
    Returns True if the document has been uploaded, False otherwise. If the return is True then it
    also returns the name of the missing documents.
    """
    # Name of the documents that should be found on GCP
    name_documents = Application.name_docs

    # Check national or international documents, if needed
    region = call.university_id.get_region_display()
    if region == 'Convenio Sigueme/Nacional':
        name_documents.append(Application.national_name_docs)

    elif region != 'Uniandes':  # It is an international call
        name_documents.append(Application.international_name_docs)

    # Check each possible file
    missing_docs = []
    for name_doc in name_documents:
        complete_name = f'{name_doc}_{student.id}_{call.id}'
        if not exists(complete_name):
            missing_docs.append(name_doc)

    if len(missing_docs) > 0:
        return False, missing_docs
    return True, missing_docs


def exists(file_name: str) -> bool:
    """
    Returns True if the given file exists in the complete_doc bucket, False otherwise.
    """
    bucket = STORAGE_CLIENT.bucket('complete_doc')
    blobs = bucket.list_blobs(prefix=file_name)
    try:
        _ = next(blobs)
        return True
    except StopIteration:
        return False
