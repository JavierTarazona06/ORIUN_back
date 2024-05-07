# Case 7: Elegir ganadores de una convocatoria

# 1. Ver pre-resultados de los postulantes, Orden General
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order/<int:pk>/`.

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


# 2. Ver pre-resultados de los postulantes, Orden Documentos
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order_docs/<int:pk>/`.

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
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order_papa/<int:pk>/`.

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
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order_adva/<int:pk>/`.

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
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order_lang/<int:pk>/`.

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
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/applications/order_pbm/<int:pk>/`.

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
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/application/winner/<int:pk>/`.

**Method:** `POST`

**Description:** Set as winner the student with application ID that equals to the given ID.

**Permissions:** Employee.

**Inputs:**

| Field Name       | Required      | Type          | Description                                          |
|------------------|---------------|---------------|------------------------------------------------------|
| `application_id` | YES - In Path | integer       | A unique integer value identifying this application. |

**Outputs:**

| Field Name | Type   | Description                                   |
|------------|--------|-----------------------------------------------|
| `message`  | string | "El estudiante fue seleccionado" or EXCEPTION |


# 8. Remover Ganador
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/application/not_winner/<int:pk>/`.

**Method:** `POST`

**Description:** Remove as winner the student with application ID that equals to the given ID.

**Permissions:** Employee.

**Inputs:**

| Field Name       | Required      | Type          | Description                                          |
|------------------|---------------|---------------|------------------------------------------------------|
| `application_id` | YES - In Path | integer       | A unique integer value identifying this application. |

**Outputs:**

| Field Name | Type   | Description                                         |
|------------|--------|-----------------------------------------------------|
| `message`  | string | "El estudiante ha sido deseleccionado" or EXCEPTION |