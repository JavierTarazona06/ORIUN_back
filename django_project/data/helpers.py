import time
import fitz
import re
import smtplib
import os
from dotenv import load_dotenv, find_dotenv
import threading
import random
import string

def delete_verif_code(path):
    time.sleep(300)  # Esperar 5 minutos (5 minutos * 60 segundos/minuto)
    if os.path.exists(path):
        os.remove(path)

def sent_email_verif_code(to:str, id):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    MAIL = "jtarazonaj@unal.edu.co"
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    caracteres = string.ascii_letters + string.digits
    verif_code = ''.join(random.choice(caracteres) for _ in range(10))

    with (smtplib.SMTP("smtp.gmail.com", 587) as smtp):
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(MAIL, MAIL_PASSWORD)

        subject = "ORIUN Verification Code"
        headers = f"From: {MAIL}\r\nTo: {to}\r\nSubject: {subject}\r\n"
        msg = f"{headers}\r\nCordial saludo,\n\nSu codigo de verificacion para acceder a la plataforma es: {verif_code}.\nRecuerde que el codigo solo dura 5 minutos activo desde la primera solicitud.\n\nAtentamente,\nEquipo ORIUN."

        smtp.sendmail(MAIL, to, msg)

    file_name = r"data/{}_verif_code.txt".format(id)
    with open(file_name, "w") as file:
        file.write(verif_code)
    borrar_thread = threading.Thread(target=delete_verif_code, args=(file_name,))
    borrar_thread.start()

    return 0

#sent_email_verif_code("javitar06@gmail.com", 1021632167)


def get_data_grades_certificate(path: str):
    """
    Get metadata from grades certificate from fitz.

    Input:
    * path: path of a pdf file to fitz

    Output:
    * Ej: {'id': '123456', 'average': '4.2', 'program': 'INGENIERÍA DE SISTEMAS Y COMPUTACIÓN', 'faculty': 'INGENIERÍA'}
    """
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    text = text.replace('�', '')

    ans = {}

    cedula_regex = r"Cédula Nº (\d+)"
    match = re.search(cedula_regex, text)
    if match:
        numero_cedula = match.group(1)
        ans["id"] = numero_cedula
    else:
        raise KeyError("No match for 'Cédula de Estudiante'")

    average_regex = r"Promedio académico: (\d+(?:\.\d+))"
    match = re.search(average_regex, text)
    if match:
        average = match.group(1)
        ans["average"] = average
    else:
        raise KeyError("No match for 'Promedio de Estudiante'")

    program_regex = r'Estudios (.*?) y ha cursado'
    match = re.search(program_regex, text)
    if match:
        program = match.group(1)
        ans["program"] = program
    else:
        program_regex = r'(.*?) y ha cursado'
        match = re.search(program_regex, text)
        if match:
            program = match.group(1)
            ans["program"] = program
        else:
            program_regex = r'Estudios (.*?) '
            match = re.search(program_regex, text)
            if match:
                program = match.group(1)
                ans["program"] = program
            else:
                raise KeyError("No match for 'Programa de Estudiante'")

    facult_regex = r'FACULTAD DE (.*?)\n'
    match = re.search(facult_regex, text)
    if match:
        facult = match.group(1)
        ans["faculty"] = facult
    else:
        raise KeyError("No match for 'Facultad de Estudiante'")

    return ans

def get_data_student_certificate(path: str):
    """
    Get metadata from student certificate from fitz.

    Input:
    * path: path of a pdf file to fitz

    Output:
    * Ej: {'id': '123456', 'advance': '50,8'}
    """
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    text = text.replace('�', '')

    ans = {}

    cedula_regex = r"Cédula Nº (\d+)"
    match = re.search(cedula_regex, text)
    if match:
        numero_cedula = match.group(1)
        ans["id"] = numero_cedula
    else:
        raise KeyError("No match for 'Cédula de Estudiante'")

    advance_regex = r"un (\b\d+,\d+\b) %"
    match = re.search(advance_regex, text)
    if match:
        advance = match.group(1)
        ans["advance"] = advance.replace(",", ".")
    else:
        raise KeyError("No match for 'Avance de Estudiante'")

    return ans

def get_data_student_payment(path: str):
    """
    Get metadata from student payment receipt from fitz.

    Input:
    * path: path of a pdf file to fitz

    Output:
    * {}
    """
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    text = text.replace('�', '')
    lines = text.split('\n')

    ans = {}

    ans["id"] = lines[2]
    if ' ' in ans["id"]:
        ans["id"] = lines[1]

    pbm_regex = r"CALCULADO\n(\b\d+\b)"
    match = re.search(pbm_regex, text)
    if match:
        pbm = match.group(1)
        ans["pbm"] = pbm
    else:
        pbm_regex = r"COLEGIO\n(\b\d+\b)"
        match = re.search(pbm_regex, text)
        if match:
            pbm = match.group(1)
            ans["pbm"] = pbm
        else:
            raise KeyError("No match for 'PBM de Estudiante'")

    admission_regex = r"\n(.*)\nCarrera 30 Nº 45 - 03"
    match = re.search(admission_regex, text)
    if match:
        admission = match.group(1)
        ans["admission"] = admission
    else:
        raise KeyError("No match for 'Tipo de admisión de Estudiante'")

    return ans


# print(get_data_grades_certificate("data/forms/templates/Certificado_Notas.pdf"))
# print(get_data_student_certificate("data/forms/templates/Matricula_Unal.pdf"))
# print(get_data_student_payment("data/forms/templates/ReciboPago.pdf"))
