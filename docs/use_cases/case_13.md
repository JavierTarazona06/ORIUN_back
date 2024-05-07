# Case 13: Registro de Usuarios

# 0. Request Verification Code
<span style="color: green; font-weight: bold;"> Done </span>

**URL:** `/person/code/`.

**Method:** `POST`

**Description:** Ask for the verification code. It is sent to the given email.

**Permissions:** Public that have an email with domain @unal.edu.co

**Inputs:** 

| Field Name | Required | Type    | Description                                   |
|------------|----------|---------|-----------------------------------------------|
| `id`       | YES      | string  | id of the person that is requesting the code  |
| `email`    | YES      | string  | Email with @unal.edu.co domain.               |

**Outputs:**

| Field Name | Type      | Description                                                                                                |
|------------|-----------|------------------------------------------------------------------------------------------------------------|
| `mensaje`  | string    | "Se envió el código de verificación al correo `indicado`, "El correo no es dominio unal.edu.co", EXCEPTIONS |

# 1. Post User Student
<span style="color: green; font-weight: bold;"> Done </span>

**URL:** `/student/post/`.

**Method:** `POST`

**Description:** Creates a new student in DB.

**Permissions:** Public that have an email with domain @unal.edu.co

**Inputs:** 

| Field Name            | Required | Type             | Description                                                             |
|-----------------------|----------|------------------|-------------------------------------------------------------------------|
| `email`               | YES      | string           | Email with @unal.edu.co domain.                                         |
| `password`            | YES      | Bytea            | It must go encrypted                                                    |
| `verif_code`          | YES      | string           | Verification code that is sent to user email                            |
| `id`                  | YES      | integer          | Cédula del estudiante.                                                  |
| `first_name`          | YES      | string           | Student First Name                                                      |
| `last_name`           | YES      | string           | Student Last Name                                                       |
| `type_document`       | YES      | enum             | Tipo del documento (CC, CE, PA).                                        |
| `birth_place`         | YES      | string           | Ciudad de nacimiento.                                                   |
| `birth_date`          | YES      | date (YYY-MM-DD) | Fecha de nacimiento del estudiante.                                     |
| `country`             | YES      | string           | País de residencia.                                                     |
| `city`                | YES      | string           | Ciudad de residencia.                                                   |
| `phone`               | YES      | string           | Teléfono de longitud de 3 a 12 carácteres numéricos.                    |
| `address`             | YES      | string           | Dirección de residencia del estudiante.                                 |
| `sex`                 | YES      | enum             | Sexo del estudiante (M, F).                                             |
| `ethnicity`           | YES      | enum             | Etnia del estudiante (IN, AF, RG, NA).                                  |
| `headquarter`         | YES      | enum             | Sede del estudiante (BO, AM, CA, MA, ME, OR, PA, TU, LP).               |
| `PAPA`                | YES      | float            | Promedio estudiante [0, 5.0]                                            |
| `PBM`                 | YES      | smallInt         | Puntaje matrícula estudiante [0,100]                                    |
| `advance`             | YES      | float            | Porcentaje avance estudiante [0,100]                                    |
| `is_enrolled`         | YES      | bool             | ¿Está matriculado a la Universidad? true or false                       |
| `num_semesters`       | YES      | smallInt         | Número de semestre/matrícula actual                                     |
| `diseases`            | YES      | String           | Detalle enfermedades del estudiante.                                    |
| `medication`          | YES      | String           | Detalle medicamentos que toma el estudiante.                            |
| `faculty`             | YES      | enum             | Facultad: Ver opciones en el link de constantes.*                       |
| `major`               | YES      | enum             | Programa: Ver opciones en el link de constantes.*                       |
| `admission`           | YES      | enum             | Tipo de admisión: Ver opciones en el link de constantes.*               |
| `study_level`         | YES      | enum             | Nivel de estudio: Ver opciones en el link de constantes.*               |
| `certificate_grades`  | YES      | document         | Documento pdf del certificado de notas expedido por el SIA (<= 3MB)     |
| `certificate_student` | YES      | document         | Documento pdf del certificado de matricula expedido por el SIA (<= 3MB) |
| `payment_receipt`     | YES      | document         | Documento pdf del recibo de pago por el SIA (<= 3MB)                    |

* Vea más info de los enums en el archivo de constantes del repo de Back (https://github.com/JavierTarazona06/ORIUN_back/blob/main/django_project/data/constants.json)

**Outputs:**

| Field Name | Type                | Description                                                                         |
|------------|---------------------|-------------------------------------------------------------------------------------|
| `mensaje`  | string              | "Estudiante creado exitosamente", "El correo no es dominio unal.edu.co", EXCEPTIONS |

# 2. Update User Student
<span style="color: gray; font-weight: bold;"> PAUSED: NOT URGENT </span>

**URL:** `/student/put/<int:pk>/`.

**Method:** `PUT`

**Description:** Updates student info according to its ID.

**Permissions:** Student which ID is in the path.

**Inputs:** 

| Field Name              | Required         | Type     | Description                                                    |
|-------------------------|------------------|----------|----------------------------------------------------------------|
| `password`              | NO               | string   | It must go encrypted                                           |
| `country`               | NO               | string   | País de residencia.                                            |
| `city`                  | NO               | string   | Ciudad de residencia.                                          |
| `phone`                 | NO               | string   | Teléfono de longitud de 3 a 12 carácteres numéricos.           |
| `address`               | NO               | string   | Dirección de residencia del estudiante.                        |
| `PAPA`                  | NO or YES - 1    | float    | Promedio estudiante [0, 5.0]                                   |
| `PBM`                   | NO or YES - 2    | Int      | Puntaje matrícula estudiante [0,100]                           |
| `advance`               | NO or YES - 3    | float    | Porcentaje avance estudiante [0,100]                           |
| `is_enrolled`           | NO               | bool     | ¿Está matriculado a la Universidad? true or false              |
| `num_semesters`         | NO               | Int      | Número de semestre/matrícula actual                            |
| `diseases`              | NO               | String   | Detalle enfermedades del estudiante.                           |
| `medication`            | NO               | String   | Detalle medicamentos que toma el estudiante.                   |
| `certificate_grades`    | NO or YES - 1    | document | Documento pdf del certificado de notas expedido por el SIA     |
| `payment_receipt`       | NO or YES - 2    | document | Documento pdf del recibo de pago por el SIA                    |
| `certificate_student`   | NO or YES - 3    | document | Documento pdf del certificado de matricula expedido por el SIA |

Yes - Required Together (N): This indicates that if at least one of these fields is provided, all other fields of the same type become mandatory.

**Outputs:**

| Field Name | Type                | Description                                       |
|------------|---------------------|---------------------------------------------------|
| `mensaje`  | string              | "Estudiante actualizado exitosamente", EXCEPTIONS |

# 3. Read User Student
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/student/get/<int:pk>/`.

**Method:** `GET`

**Description:** Returns data related to student according to the given ID.

**Permissions:** Student which ID is in the path.

**Inputs:**

| Field Name           | Required      | Type          | Description                                      |
|----------------------|---------------|---------------|--------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this student. |

**Outputs:** 

| Field Name             | Type                     | Description                                                                         |
|------------------------|--------------------------|-------------------------------------------------------------------------------------|
| `email`                | string                   | Email with @unal.edu.co domain.                                                     |
| `id`                   | integer                  | Cédula del estudiante.                                                              |
| `first_name`           | string                   | Student First Name                                                                  |
| `last_name`            | string                   | Student Last Name                                                                   |
| `type_document`        | enum                     | Tipo del documento (CC, CE, PA).                                                    |
| `birth_place`          | string                   | Ciudad de nacimiento.                                                               |
| `birth_date`           | date (YYY-MM-DD)         | Fecha de nacimiento del estudiante.                                                 |
| `country`              | string                   | País de residencia.                                                                 |
| `city`                 | string                   | Ciudad de residencia.                                                               |
| `phone`                | string                   | Teléfono de longitud de 3 a 12 carácteres numéricos.                                |
| `address`              | string                   | Dirección de residencia del estudiante.                                             |
| `sex`                  | enum                     | Sexo del estudiante (M, F).                                                         |
| `ethnicity`            | enum                     | Etnia del estudiante (IN, AF, RG, NA).                                              |
| `headquarter`          | enum                     | Sede del estudiante (BO, AM, CA, MA, ME, OR, PA, TU, LP).                           |
| `PAPA`                 | float                    | Promedio estudiante [0, 5.0]                                                        |
| `PBM`                  | Int                      | Puntaje matrícula estudiante [0,100]                                                |
| `advance`              | float                    | Porcentaje avance estudiante [0,100]                                                |
| `calls_done`           | list of dict [{}, {}...] | Convocatorias realizadas por el estudiante                                          |
| {`call_id`             | int                      | ID de la convocatoria                                                               |
| `university_name`      | string                   | Nombre de la universidad de la convocatoria                                         |
| `study_level`          | enum                     | Nivel de estudio de la convocatoria: Ver opciones en el link de constantes.*        |
| `year`                 | int                      | Año de la convocatoria                                                              |
| `semester`             | int                      | Semestre de la convocatoria                                                         |
| `description`}         | string                   | Descripción de la convocatoria                                                      |
| `is_enrolled`          | bool                     | ¿Está matriculado a la Universidad? true or false                                   |
| `date_banned_mobility` | date                     | Si fue vetado, fecha del último veto                                                |
| `num_semesters`        | Int                      | Número de semestre/matrícula actual                                                 |
| `diseases`             | String                   | Detalle enfermedades del estudiante.                                                |
| `medication`           | String                   | Detalle medicamentos que toma el estudiante.                                        |
| `faculty`              | enum                     | Facultad: Ver opciones en el link de constantes.*                                   |
| `major`                | enum                     | Programa: Ver opciones en el link de constantes.*                                   |
| `admission`            | enum                     | Tipo de admisión: Ver opciones en el link de constantes.*                           |
| `study_level`          | enum                     | Nivel de estudio: Ver opciones en el link de constantes.*                           |
| `certificate_grades`   | string                   | Link Documento pdf del certificado de notas expedido por el SIA                     |
| `certificate_student`  | string                   | Link Documento pdf del certificado de matricula expedido por el SIA                 |
| `payment_receipt`      | string                   | Link Documento pdf del recibo de pago por el SIA                                    |

* Vea más info de los enums en el archivo de constantes del repo de Back (https://github.com/JavierTarazona06/ORIUN_back/blob/main/django_project/data/constants.json)


# 4. Post User Employee
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/employee/post/`.

**Method:** `POST`

**Description:** Creates a new employee in DB.

**Permissions:** Public that have an email with domain @unal.edu.co

**Condition:** Email must be in the DB of the program, that means the staff must be previously in the DB.

**Inputs:** 

| Field Name      | Required | Type             | Description                                                |
|-----------------|----------|------------------|------------------------------------------------------------|
| `email`         | YES      | string           | Email with @unal.edu.co domain.                            |
| `password`      | YES      | Bytea            | It must go encrypted                                       |
| `verif_code`    | YES      | string           | Verification code that is sent to user email               |
| `id`            | YES      | integer          | Cédula del funcionario.                                    |
| `first_name`    | YES      | string           | Employee First Name                                        |
| `last_name`     | YES      | string           | Employee Last Name                                         |
| `type_document` | YES      | enum             | Tipo del documento (CC, CE, PA).                           |
| `birth_place`   | YES      | string           | Ciudad de nacimiento.                                      |
| `birth_date`    | YES      | date (YYY-MM-DD) | Fecha de nacimiento del estudiante.                        |
| `country`       | YES      | string           | País de residencia.                                        |
| `city`          | YES      | string           | Ciudad de residencia.                                      |
| `phone`         | YES      | string           | Teléfono de longitud de 3 a 12 carácteres numéricos.       |
| `address`       | YES      | string           | Dirección de residencia del funcionario.                   |
| `sex`           | YES      | enum             | Sexo del funcionario (M, F).                               |
| `ethnicity`     | YES      | enum             | Etnia del funcionario (IN, AF, RG, NA).                    |
| `headquarter`   | YES      | enum             | Sede del funcionario (BO, AM, CA, MA, ME, OR, PA, TU, LP). |
| `dependency`    | YES      | enum             | Dependencia del funcionario (ORI, DRE).                    |

* Vea más info de los enums en el archivo de constantes del repositorio de Back (https://github.com/JavierTarazona06/ORIUN_back/blob/main/django_project/data/constants.json)

**Outputs:**

| Field Name | Type                | Description                                                                          |
|------------|---------------------|--------------------------------------------------------------------------------------|
| `mensaje`  | string              | "Funcionario creado exitosamente", "El correo no es dominio unal.edu.co", EXCEPTIONS |

# 5. Update User Employee
<span style="color: gray; font-weight: bold;"> PAUSED: NOT URGENT </span>

**URL:** `/employee/put/<int:pk>/`.

**Method:** `PUT`

**Description:** Updates employee info according to its ID.

**Permissions:** Employee which ID is in the path.

**Inputs:** 

| Field Name              | Required         | Type                | Description                                          |
|-------------------------|------------------|---------------------|------------------------------------------------------|
| `password`              | NO               | string              | It must go encrypted                                 |
| `country`               | NO               | string              | País de residencia.                                  |
| `city`                  | NO               | string              | Ciudad de residencia.                                |
| `phone`                 | NO               | string              | Teléfono de longitud de 3 a 12 carácteres numéricos. |
| `address`               | NO               | string              | Dirección de residencia del funcionario.             |

Yes - Required Together (N): This indicates that if at least one of these fields is provided, all other fields of the same type become mandatory.

**Outputs:**

| Field Name | Type                | Description                                        |
|------------|---------------------|----------------------------------------------------|
| `mensaje`  | string              | "Funcionario actualizado exitosamente", EXCEPTIONS |

# 6. Read User Employee
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/employee/get/<int:pk>/`.

**Method:** `GET`

**Description:** Returns data related to employee according to the given ID.

**Permissions:** Employee which ID is in the path.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                       |
|----------------------|---------------|---------------|---------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this employee. |

**Outputs:** 

| Field Name           | Type             | Description                                             |
|----------------------|------------------|---------------------------------------------------------|
| `email`              | string           | Email with @unal.edu.co domain.                         |
| `ID`                 | integer          | Cédula del Employee.                                    |
| `first_name`         | string           | Employee First Name                                     |
| `last_name`          | string           | Employee Last Name                                      |
| `type_document`      | enum             | Tipo del documento (CC, CE, PA).                        |
| `birth_place`        | string           | Ciudad de nacimiento.                                   |
| `birth_date`         | date (YYY-MM-DD) | Fecha de nacimiento del Employee.                       |
| `country`            | string           | País de residencia.                                     |
| `city`               | string           | Ciudad de residencia.                                   |
| `phone`              | string           | Teléfono de longitud de 3 a 12 carácteres numéricos.    |
| `address`            | string           | Dirección de residencia del  Employee.                  |
| `sex`                | enum             | Sexo del Employee (M, F).                               |
| `ethnicity`          | enum             | Etnia del Employee (IN, AF, RG, NA).                    |
| `headquarter`        | enum             | Sede del Employee (BO, AM, CA, MA, ME, OR, PA, TU, LP). |


* Vea más info de los enums en el archivo de constantes del repo de Back (https://github.com/JavierTarazona06/ORIUN_back/blob/main/django_project/data/constants.json)