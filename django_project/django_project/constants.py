import os
import json


class Constants:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, 'constants.json'), 'r', encoding='UTF-8') as file:
        constants_dict = json.load(file)

    with open(os.path.join(base_dir, 'info_faculties.json'), 'r', encoding='UTF-8') as file:
        INFO_FACULTIES = json.load(file)

    # Person
    SEX_CHOICES = constants_dict["sex_en"]
    TYPE_DOC_CHOICES = constants_dict["typ_doc_en"]
    ETHNICITY_CHOICES = constants_dict["ethnicity_en"]
    TYPE_USER_CHOICES = constants_dict["type_user_en"]

    # Study
    HEADQUARTER_CHOICES = constants_dict["headquarter_en"]
    FACULTY_CHOICES = constants_dict["faculty_en"]
    MAJOR_CHOICES = constants_dict["major_en"]
    DEPENDENCE_CHOICES = constants_dict["dependence_en"]
    ADMISSION_CHOICES = constants_dict["admission_en"]
    STUDY_LEVEL_CHOICES = constants_dict["study_level_en"]

    # About Calls And Applications
    REGION_CHOICES = constants_dict["regions_en"]
    FORMAT_CHOICES = constants_dict["format_en"]
    LANGUAGE_CHOICES = constants_dict["language_en"]
    SEMESTER_CHOICES = constants_dict["semester_en"]

    # Names of forms
    NAME_FORMS = {
        'autorización_tratamiento_datos_personales': 'ATDP',
        'formato_corresponsabilidad_saliente_nacional': 'FCSN',
        'formato_movilidad_saliente_cursar_asignaturas': 'FMSCA',
        'formulario_pregrado_sígueme': 'FPS'
    }
