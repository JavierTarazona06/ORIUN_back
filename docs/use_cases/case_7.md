# Case 7: Elegir ganadores de una convocatoria

Códigos Axios: https://docs.google.com/document/d/1dAn8UFItyqq34QpMD-qJw1PwswaAh9L6zcSQaDYI02Y/edit#heading=h.986fwnir0p28

pre-resultados son las Aplicaciones

# 1. Ver pre-resultados de los postulantes, Orden General
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in general order according to the given call ID.

**Permissions:** Employee.

**Inputs:** 

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |

# 1.1 Ver pre-resultados de los postulantes, sin Orden
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/get_all/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) without order according to the given call ID.

**Permissions:** Employee.

**Inputs:** 

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |

# 2. Ver pre-resultados de los postulantes, Orden Documentos
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order_docs/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in docs order according to the given call ID.

**Permissions:** Employee.

**Inputs:**

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |


# 3. Ver pre-resultados de los postulantes, Orden PAPA
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order_papa/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in PAPA order according to the given call ID.

**Permissions:** Employee.

**Inputs:**

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |


# 4. Ver pre-resultados de los postulantes, Orden Avance
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order_adva/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in advance order according to the given call ID.

**Permissions:** Employee.

**Inputs:**

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |



# 5. Ver pre-resultados de los postulantes, Orden Idioma
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order_lang/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in language order according to the given call ID.

**Permissions:** Employee.

**Inputs:** 

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |


# 6. Ver pre-resultados de los postulantes, Orden PBM
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/order_pbm/<int:pk>/`.

**Method:** `GET`

**Description:** Returns students applications (pre-results) in PBM order according to the given call ID.

**Permissions:** Employee.

**Inputs:**

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name            | Type   | Description                                                                                     |
|-----------------------|--------|-------------------------------------------------------------------------------------------------|
| `id`                  | int    | Application unique ID                                                                           |
| `student_id`          | int    | Students unique ID                                                                              |
| `student_name`        | string | Nombre del estudiante.                                                                          |
| `state_documents `    | int    | Estado de la documentación (0: no revisados 1: modificación solicitada 2: documentos aprobados) |
| `student_PAPA`        | float  | PAPA del estudiante                                                                             |
| `student_advance`     | float  | Avance en porcentaje del estudiante.                                                            |
| `student_headquarter` | string | Sede del estudiante.                                                                            |
| `language`            | bool   | ¿Cumple con el requisito de idioma? true / false                                                |
| `student_PBM`         | int    | PBM del estudiante                                                                              |


# 7. Asignar Ganador
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/winner/`.

**Method:** `POST`

**Description:** Set as winner the student with application ID that equals to the given student ID.
The endpoint Check Available Slots,  Set Winner, Close the call and Send email.
Modify Highest and minimum PAPA winner in Call

**Permissions:** Employee.

**Inputs:** In body request

| Field Name   | Required | Type          | Description                                                   |
|--------------|----------|---------------|---------------------------------------------------------------|
| `call_id`    | YES      | integer       | A unique integer value identifying this call application.     |
| `student_id` | YES      | integer       | A unique integer value identifying the student who is winner. |

**Outputs:**

| Field Name | Type   | Description                                                                                      |
|------------|--------|--------------------------------------------------------------------------------------------------|
| `message`  | string | "El estudiante con id {student_id} fue seleccionado para la convocatoria {call_id}" or EXCEPTION |


# 8. Remover Ganador o dejarlo como no ganador
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/not_winner/`.

**Method:** `POST`

**Description:** Remove as winner (or set not winner) the student with application ID that equals to the given student ID and send email.
Modify Highest and minimum PAPA winner in Call

**Permissions:** Employee.

**Inputs:** In body.

| Field Name   | Required | Type        | Description                                                               |
|--------------|----------|-------------|---------------------------------------------------------------------------|
| `call_id`    | YES      | integer     | A unique integer value identifying this call application.                 |
| `student_id` | YES      | integer     | A unique integer value identifying the student who is no longer a winner. |

**Outputs:**

| Field Name | Type   | Description                                                                                          |
|------------|--------|------------------------------------------------------------------------------------------------------|
| `message`  | string | "El estudiante con id {student_id} fue des-seleccionado para la convocatoria {call_id}" or EXCEPTION |


# 9. Cerrar Convocatoria
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/call/set_closed/`.

**Method:** `POST`

**Description:** Set a call as closed.

**Permissions:** Employee.

**Inputs:** In body.

| Field Name   | Required | Type        | Description                                   |
|--------------|----------|-------------|-----------------------------------------------|
| `call_id`    | YES      | integer     | A unique integer value identifying this call. |

**Outputs:**

| Field Name | Type   | Description                                                                                                                                     |
|------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `message`  | string | "Se cerró la convocatoria con ID: {call_id} de la universidad: {call.university_name} en el periodo: {call.year}-{call.semester}." or EXCEPTION |

# 10. Abrir Convocatoria
<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/call/set_open/`.

**Method:** `POST`

**Description:** Set a call as open.

**Permissions:** Employee.

**Inputs:** In body.

| Field Name   | Required | Type        | Description                                   |
|--------------|----------|-------------|-----------------------------------------------|
| `call_id`    | YES      | integer     | A unique integer value identifying this call. |

**Outputs:**

| Field Name | Type   | Description                                                                                                                                     |
|------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `message`  | string | "Se abrió la convocatoria con ID: {call_id} de la universidad: {call.university_name} en el periodo: {call.year}-{call.semester}." or EXCEPTION |

# 11. Verificación para asignar ganadores

<span style="color: green; font-weight: bold;"> DONE </span>

**URL:** `/application/pre_assign_winners/<int:pk>/`.

**Method:** `GET`

**Description:** Verifies if all students were checked over by employees.

**Permissions:** Employee.

**Inputs:** 

| Field Name | Required      | Type          | Description                                   |
|------------|---------------|---------------|-----------------------------------------------|
| `call_id`  | YES - In Path | integer       | A unique integer value identifying this call. |

**Outputs:**

| Field Name | Type | Description                                                                                                                |
|------------|------|----------------------------------------------------------------------------------------------------------------------------|
| `message`  | dict | All applications were reviwed.<br/> value: "Ya se revisaron todas las aplicaciones, se pueden asignar los ganadores"       |

| Field Name | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Error`    | dict | All applications are not reviwed.<br/> Example Value: <br/>"OriunError: Hay estudiantes que tienen aplicaciones pendientes por revisar. Aún no se puede asignar ganador. Estudiantes: [{'id': 3, 'student_id': '106985477', 'student_name': 'Isabella Gonzalez', 'state_documents': 0, 'student_PAPA': 3.0, 'student_advance': 10.0, 'student_headquarter': 'BO', 'language': False, 'student_PBM': 50}]"     |