# Case 2: Convocatorias (CRUD)

# 1.  Get Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/`.

**Method:** `GET`

**Description:** Return all calls.

**Permissions:** Employee and Admin

**Inputs:** NONE 

**Outputs:**

| Field Name            | Type    | Description                                               |
|-----------------------|---------|-----------------------------------------------------------|
| `university_id`       | int     | ID of the University offering the call.                   | 
| `active`              | bool    | True if is active, false otherwise                        |
| `begin_date`          | Date    | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date    | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float   | Minimum advance required for application.                 |
| `min_papa`            | Float   | Minimum PAPA score required for application.              |
| `format`              | String  | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String  | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer | Year of the exchange.                                     |
| `semester`            | Integer | Semester of the exchange. (1,2)                           |
| `language`            | String  | Language of the call according to ISO 639-1               |
| `description`         | Text    | Description of the call.                                  |
| `available_slots`     | Integer | Number of available slots for the call.                   |
| `note`                | Text    | Additional notes about the call.                          |
| `highest_papa_winner` | Float   | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float   | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer | Number of winners.                                        |
| `flag_image_url`      | URL     | Flag URL.                                                 |


# 2.  Post Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/`.

**Method:** `POST`

**Description:** Create a call.

**Permissions:** Employee and Admin

**Inputs:**

| Field Name            | Required  | Type          | Description                                                |
|-----------------------|-----------|---------------|------------------------------------------------------------|
| `university_id`       | YES       | int           | ID of the University offering the call.                    | 
| `active`              | YES       | bool          | True if is active, false otherwise                         |
| `begin_date`          | YES       | Date          | Calls start date.(YYYY-MM-DD)                              |
| `deadline`            | YES       | Date          | Calls deadline date for submission.(YYYY-MM-DD)            |
| `min_advance`         | YES       | Float         | Minimum advance required for application.                  |
| `min_papa`            | YES       | Float         | Minimum PAPA score required for application.               |
| `format`              | YES       | String        | Format of the call(virtual,presencial or mixed).           |
| `study_level`         | YES       | String        | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
| `year`                | YES       | Integer       | Year of the exchange.                                      |
| `semester`            | YES       | Integer       | Semester of the exchange. (1,2)                            |
| `language`            | YES       | String        | Language of the call according to ISO 639-1                |
| `description`         | YES       | Text          | Description of the call.                                   |
| `available_slots`     | YES       | Integer       | Number of available slots for the call.                    |
| `note`                | NO        | Text          | Additional notes about the call.                           |
| `highest_papa_winner` | NO        | Float         | Highest PAPA score among winners of the call.              |
| `minimum_papa_winner` | NO        | Float         | Minimum PAPA score among winners of the call.              |
| `selected`            | NO        | Integer       | Number of winners.                                         |


**Outputs:**

| Field Name            | Type          | Description                                                |
|-----------------------|---------------|------------------------------------------------------------|
| `university_id`       | int           | ID of the University offering the call.                    | 
| `active`              | bool          | True if is active, false otherwise                         |
| `begin_date`          | Date          | Calls start date.(YYYY-MM-DD)                              |
| `deadline`            | Date          | Calls deadline date for submission.(YYYY-MM-DD)            |
| `min_advance`         | Float         | Minimum advance required for application.                  |
| `min_papa`            | Float         | Minimum PAPA score required for application.               |
| `format`              | String        | Format of the call(virtual,presencial or mixed).           |
| `study_level`         | String        | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
| `year`                | Integer       | Year of the exchange.                                      |
| `semester`            | Integer       | Semester of the exchange. (1,2)                            |
| `language`            | String        | Language of the call according to ISO 639-1                |
| `description`         | Text          | Description of the call.                                   |
| `available_slots`     | Integer       | Number of available slots for the call.                    |
| `note`                | Text          | Additional notes about the call.                           |
| `highest_papa_winner` | Float         | Highest PAPA score among winners of the call.              |
| `minimum_papa_winner` | Float         | Minimum PAPA score among winners of the call.              |
| `selected`            | Integer       | Number of winners.                                         |


# 3.  Get Call by ID: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/<int:pk>/`.

**Method:** `GET`

**Description:** Get a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                |
|----------------------|---------------|---------------|------------------------------------------------------------|
| `call_id`            | YES - In Path | int           | ID of the call to be updated.                              |


**Outputs:**

| Field Name            | Type    | Description                                               |
|-----------------------|---------|-----------------------------------------------------------|
| `id`                  | int     | ID of the call.                                           | 
| `university_id`       | int     | ID of the University offering the call.                   | 
| `active`              | bool    | True if is active, false otherwise                        |
| `begin_date`          | Date    | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date    | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float   | Minimum advance required for application.                 |
| `min_papa`            | Float   | Minimum PAPA score required for application.              |
| `format`              | String  | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String  | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer | Year of the exchange.                                     |
| `semester`            | Integer | Semester of the exchange. (1,2)                           |
| `language`            | String  | Language of the call according to ISO 639-1               |
| `description`         | Text    | Description of the call.                                  |
| `available_slots`     | Integer | Number of available slots for the call.                   |
| `note`                | Text    | Additional notes about the call.                          |
| `highest_papa_winner` | Float   | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float   | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer | Number of winners.                                        |
| `flag_image_url`      | URL     | Flag URL.                                                 |


# 4.  Update Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api_put/<int:pk>/`.

**Method:** `PUT`

**Description:** Update a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name            | Required      | Type          | Description                                                |
|-----------------------|---------------|---------------|------------------------------------------------------------|
| `call_id`             | YES - In Path | int           | ID of the call to be updated.                              |
| `university_id`       | NO            | int           | ID of the University offering the call.                    | 
| `active`              | NO            | bool          | True if is active, false otherwise                         |
| `begin_date`          | NO            | Date          | Calls start date.(YYYY-MM-DD)                              |
| `deadline`            | NO            | Date          | Calls deadline date for submission.(YYYY-MM-DD)            |
| `min_advance`         | NO            | Float         | Minimum advance required for application.                  |
| `min_papa`            | NO            | Float         | Minimum PAPA score required for application.               |
| `format`              | NO            | String        | Format of the call(virtual,presencial or mixed).           |
| `study_level`         | NO            | String        | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
| `year`                | NO            | Integer       | Year of the exchange.                                      |
| `semester`            | NO            | Integer       | Semester of the exchange. (1,2)                            |
| `language`            | NO            | String        | Language of the call according to ISO 639-1                |
| `description`         | NO            | Text          | Description of the call.                                   |
| `available_slots`     | NO            | Integer       | Number of available slots for the call.                    |
| `note`                | NO            | Text          | Additional notes about the call.                           |
| `highest_papa_winner` | NO            | Float         | Highest PAPA score among winners of the call.              |
| `minimum_papa_winner` | NO            | Float         | Minimum PAPA score among winners of the call.              |
| `selected`            | NO            | Integer       | Number of winners.                                         |


**Outputs:**

| Field Name           | Type          | Description                                                |
|----------------------|---------------|------------------------------------------------------------|
|`id`                  | int           | ID of the call.                                            | 
|`university_id`       | int           | ID of the University offering the call.                    | 
| `active`             | bool          | True if is active, false otherwise                         |
| `begin_date`         | Date          | Calls start date.(YYYY-MM-DD)                              |
| `deadline`           | Date          | Calls deadline date for submission.(YYYY-MM-DD)            |
| `min_advance`        | Float         | Minimum advance required for application.                  |
| `min_papa`           | Float         | Minimum PAPA score required for application.               |
| `format`             | String        | Format of the call(virtual,presencial or mixed).           |
| `study_level`        | String        | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
| `year`               | Integer       | Year of the exchange.                                      |
| `semester`           | Integer       | Semester of the exchange. (1,2)                            |
| `language`           | String        | Language of the call according to ISO 639-1                |
| `description`        | Text          | Description of the call.                                   |
| `available_slots`    | Integer       | Number of available slots for the call.                    |
| `note`               | Text          | Additional notes about the call.                           |
| `highest_papa_winner`| Float         | Highest PAPA score among winners of the call.              |
| `minimum_papa_winner` | Float         | Minimum PAPA score among winners of the call.              |
| `selected`           | Integer       | Number of winners.                                         |


# 5.  Delete Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                      |
|----------------------|---------------|---------------|--------------------------------------------------|
|`call_id`             | YES - In Path | int           | ID of the call to be updated.                    |


**Outputs:** None


# 6.  Open Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/opened/`.

**Method:** `GET`

**Description:** Return open calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name            | Type     | Description                                               |
|-----------------------|----------|-----------------------------------------------------------|
| `id`                  | int      | ID of the call.                                           | 
| `university_id`       | int      | ID of the University offering the call.                   | 
| `active`              | bool     | True if is active, false otherwise                        |
| `begin_date`          | Date     | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date     | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float    | Minimum advance required for application.                 |
| `min_papa`            | Float    | Minimum PAPA score required for application.              |
| `format`              | String   | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String   | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer  | Year of the exchange.                                     |
| `semester`            | Integer  | Semester of the exchange. (1,2)                           |
| `language`            | String   | Language of the call according to ISO 639-1               |
| `description`         | Text     | Description of the call.                                  |
| `available_slots`     | Integer  | Number of available slots for the call.                   |
| `note`                | Text     | Additional notes about the call.                          |
| `highest_papa_winner` | Float    | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float    | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer  | Number of winners.                                        |
| `flag_image_url`      | URL      | Flag URL.                                                 |


# 7.  Closed Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/closed/`.

**Method:** `GET`

**Description:** Return closed calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name             | Type    | Description                                               |
|------------------------|---------|-----------------------------------------------------------|
| `id`                   | int     | ID of the call.                                           | 
| `university_id`        | int     | ID of the University offering the call.                   | 
| `active`               | bool    | True if is active, false otherwise                        |
| `begin_date`           | Date    | Calls start date.(YYYY-MM-DD)                             |
| `deadline`             | Date    | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`          | Float   | Minimum advance required for application.                 |
| `min_papa`             | Float   | Minimum PAPA score required for application.              |
| `format`               | String  | Format of the call(virtual,presencial or mixed).          |
| `study_level`          | String  | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                 | Integer | Year of the exchange.                                     |
| `semester`             | Integer | Semester of the exchange. (1,2)                           |
| `language`             | String  | Language of the call according to ISO 639-1               |
| `description`          | Text    | Description of the call.                                  |
| `available_slots`      | Integer | Number of available slots for the call.                   |
| `note`                 | Text    | Additional notes about the call.                          |
| `highest_papa_winner`  | Float   | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner`  | Float   | Minimum PAPA score among winners of the call.             |
| `selected`             | Integer | Number of winners.                                        |
| `flag_image_url`       | URL     | Flag URL.                                                 |

# 8.  Filter Over Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/employee_filter/`.

**Method:** `GET`

**Description:** Return calls filtered by if is active, university_id, university_name, deadline, format, study_level, year
        semester, region, country, language.

**Permissions:** Employee and Admin.

**Inputs:**

| Field Name        | Required      | Type           | Description                                                |
|-------------------|---------------|----------------|------------------------------------------------------------|
| `active`          | Optional      | bool           | True if is active, false otherwise.                        |
| `university_id`   | Optional      | int            | ID of the University offering the call.                    |
| `university_name` | Optional      | String         | Name of the University offering the call.                  |
| `deadline`        | Optional      | date           | Calls deadline date for submission.(YYYY-MM-DD)            |
| `formato`         | Optional      | String (Enum)  | Format of the call(virtual,presencial or mixed).           |
| `study_level`     | Optional      | String (Enum)  | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
| `year`            | Optional      | int            | Year of the exchange.                                      |
| `semester`        | Optional      | int            | Semester of the exchange. (1,2)                            |
| `region`          | Optional      | String (Enum)  | University region.*                                        |
| `country`         | Optional      | String         | University country.                                        |
| `language`        | Optional      | String (Enum)  | Language that is demanded by the call.                     |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


**Outputs:** 

| Field Name            | Type    | Description                                                   |
|-----------------------|---------|---------------------------------------------------------------|
| `id`                  | int     | ID of the call.                                               | 
| `university_id`       | int     | ID of the University offering the call.                       | 
| `active`              | bool    | True if is active, false otherwise                            |
| `begin_date`          | Date    | Calls start date.(YYYY-MM-DD)                                 |
| `deadline`            | Date    | Calls deadline date for submission less than the given param. |
| `min_advance`         | Float   | Minimum advance required for application.                     |
| `min_papa`            | Float   | Minimum PAPA score required for application.                  |
| `format`              | String  | Format of the call(virtual,presencial or mixed).              |
| `study_level`         | String  | Value from (pre_pregrado,pos_postgrado or doc_doctorado).     |
| `year`                | Integer | Year of the exchange.                                         |
| `semester`            | Integer | Semester of the exchange. (1,2)                               |
| `language`            | String  | Language of the call according to ISO 639-1                   |
| `description`         | Text    | Description of the call.                                      |
| `available_slots`     | Integer | Number of available slots for the call.                       |
| `note`                | Text    | Additional notes about the call.                              |
| `highest_papa_winner` | Float   | Highest PAPA score among winners of the call.                 |
| `minimum_papa_winner` | Float   | Minimum PAPA score among winners of the call.                 |
| `selected`            | Integer | Number of winners.                                            |
| `flag_image_url`      | URL     | Flag URL.                                                     |

# 9.  Get Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/`.

**Method:** `GET`

**Description:** Return universities.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name           | Type          | Description                                                  |
|----------------------|---------------|--------------------------------------------------------------|
| `id`                 | int           | ID of the University.                                        | 
| `name`               | String        | Name of the University.                                      |
| `webpage`            | String        | Main webpage of the University.                              |
| `region`             | String (Enum) | Region of the University.*                                   |
| `country`            | String        | Country of the University.                                   |
| `city`               | String        | City of the University.                                      |
| `academic_offer`     | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | String        | Link to the university's webpage for its exchange info.      |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


# 10.  Create Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/`.

**Method:** `POST`

**Description:** Create a university.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `name`               | YES           | String        | Name of the University.                                      |
| `webpage`            | YES           | String        | Main webpage of the University.                              |
| `region`             | YES           | String (Enum) | Region of the University.*                                   |
| `country`            | YES           | String        | Country of the University.                                   |
| `city`               | YES           | String        | City of the University.                                      |
| `academic_offer`     | YES           | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | YES           | String        | Link to the university's webpage for its exchange info.      |


**Outputs:** 

| Field Name           | Type          | Description                                                  |
|----------------------|---------------|--------------------------------------------------------------|
| `id`                 | int           | ID of the University.                                        | 
| `name`               | String        | Name of the University.                                      |
| `webpage`            | String        | Main webpage of the University.                              |
| `region`             | String (Enum) | Region of the University.*                                   |
| `country`            | String        | Country of the University.                                   |
| `city`               | String        | City of the University.                                      |
| `academic_offer`     | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | String        | Link to the university's webpage for its exchange info.      |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


# 11.  Get University by ID: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `GET`

**Description:** Get a university according to given ID.

**Permissions:** Employee and Admin.

**Inputs:**

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |


**Outputs:**

| Field Name           | Type          | Description                                                  |
|----------------------|---------------|--------------------------------------------------------------|
| `id`                 | int           | ID of the University.                                        | 
| `name`               | String        | Name of the University.                                      |
| `webpage`            | String        | Main webpage of the University.                              |
| `region`             | String (Enum) | Region of the University.*                                   |
| `country`            | String        | Country of the University.                                   |
| `city`               | String        | City of the University.                                      |
| `academic_offer`     | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | String        | Link to the university's webpage for its exchange info.      |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


# 12.  Update Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api_put/<int:pk>/`.

**Method:** `PUT`

**Description:** Update a university according to given ID.

**Permissions:** Employee and Admin.

**Inputs:**

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |
| `name`               | YES           | String        | Name of the University.                                      |
| `webpage`            | YES           | String        | Main webpage of the University.                              |
| `region`             | YES           | String (Enum) | Region of the University.*                                   |
| `country`            | YES           | String        | Country of the University.                                   |
| `city`               | YES           | String        | City of the University.                                      |
| `academic_offer`     | YES           | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | YES           | String        | Link to the university's webpage for its exchange info.      |


**Outputs:** 

| Field Name           | Type          | Description                                                  |
|----------------------|---------------|--------------------------------------------------------------|
| `id`                 | int           | ID of the University.                                        | 
| `name`               | String        | Name of the University.                                      |
| `webpage`            | String        | Main webpage of the University.                              |
| `region`             | String (Enum) | Region of the University.*                                   |
| `country`            | String        | Country of the University.                                   |
| `city`               | String        | City of the University.                                      |
| `academic_offer`     | String        | Link to the university's webpage for its academic offerings. |
| `exchange_info`      | String        | Link to the university's webpage for its exchange info.      |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


# 13.  Delete Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None
