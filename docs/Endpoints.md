# Endpoints for ORIUN

## 1. Endpoint logging
**URL:** `api-token/`

**Method:** `POST`

**Description:** Used to get a JWT for later requests, it allows the backend to 
recognize the current user.

**Inputs:**

| Name       | Type   | Description                                 |
|------------|--------|---------------------------------------------|
| `username` | String | username without email info (@unal.edu.co). |
| `password` | String | password of the email.                      |

**Outputs:**

| Name        | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| `access`    | String | JWT token for authentication.                                |
| `refresh`   | String | JWT token used to refresh the access token once it expires.  |
| `type_user` | String | Indicates if the current user is an `student` or `employee`. |


## 2. Endpoint refresh token
**URL:** `api-token/refresh/`

**Method:** `POST`

**Description:** Used to regenerate the JWT access.

**Inputs:**

| Name       | Type   | Description                                 |
|------------|--------|---------------------------------------------|
| `refresh`  | String | JWT refresh given in the previous endpoint. |

**Outputs:**

| Name        | Type   | Description                       |
|-------------|--------|-----------------------------------|
| `access`    | String | new JWT token for authentication. |


## 3. Endpoint filter and display open calls
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/call/open/`. 
    
**Method:** `GET`

**Description:**  Used to filter and display open calls based on several criteria, such as  country, language requirement, university name, call_id, region and deadline. Retrieves a list of open calls based on the provided criteria.

**Inputs:**  These inputs (parameters) are not mandatory, since they are only filters. That means that you can send no filter, one filter, some of them or all of them. 


| Parameter         | Description                                                                                                                     | Type       | Required | Example                                        |   
|-------------------|---------------------------------------------------------------------------------------------------------------------------------|------------|----------|------------------------------------------------|
| `countries`       | Country of the university. First of each word in Capital letters.                                                               | String     | No       | countries=Colombia                             |
| `languages`       | Language requirement for the call                                                                                               | ArrayField | No       | languages=es                                   |
| `university_name` | Name of the university                                                                                                          | String     | No       | name_university=Universidad%20de%20los%20Andes |
| `call_id`         | ID of the call                                                                                                                  | String     | No       | 3                                              |
| `region`          | Region of the university                                                                                                        | String     | No       | 'LA' for Latin America                         |
| `deadline`        | The program will display calls with a deadline before or equal to the specified parameter and after or equal to current date.   | Date       | No       | '2022-04-26' : YYYY-MM-DD                      |


**Outputs:**

| Name              | Type        | Description                                                   |
|-------------------|-------------|---------------------------------------------------------------|
| `university_name` | String      | Name of the university offering the call.                     |
| `country`         | String      | Country where the call is offered.                            |
| `language`        | ArrayField  | Language requirement for the call.                            |
| `deadline`        | Date        | Deadline for application submission for the call.(YYYY-MM-DD) |



## 4. Endpoint filter and display closed calls
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/call/closed/`. 

**Method:** `GET`

**Description:**  Used to filter and display close calls based on several criteria, such as country, language requirement, region and university name. Retrieves a list of closed calls based on the provided criteria.

**Inputs:** These inputs(paramaters) are not mandatory, since they are only filters. That means that you can send no filter, one filter, some of them or all of them. 

| Parameter         | Description                                                       | Type       | Required | Example                                        |   
|-------------------|-------------------------------------------------------------------|------------|----------|------------------------------------------------|
| `country`         | Country of the university. First of each word in Capital letters. | String     | No       | country=Colombia                               |
| `language `       | Language requirement for the call                                 | ArrayField | No       | language=es                                    |
| `university_name` | Name of the university                                            | String     | No       | name_university=Universidad%20de%20los%20Andes |
| `region`          | Region of the university                                          | String     | No       | 'LA' for Latin America                         |

**Outputs:**

| Field Name            | Data Type    | Description                                                     |
|-----------------------|--------------|-----------------------------------------------------------------|
| `university_name`     | String       | Name of the university offering the call.                       |
| `country`             | String       | Country where the call is offered.                              |
| `language`            | ArrayField   | Language requirement for the call.                              |
| `deadline`            | Date         | Deadline for application submission for the call.(YYYY-MM-DD)   |
| `minimum_papa_winner` | Float        | Minimum PAPA score among winners of the call.                   |

# 5.  Get details of open call
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/call/open/<id>/`.  The `id` is the identification of the selected call.

**Method:** `GET`

**Description:**  Used to view all details of the specific open call. 

**Inputs:** None

**Outputs:**

| Field Name        | Type          | Description                                           |
|-------------------|---------------|-------------------------------------------------------|
|`university_name`  | String        | Name of the university offering the call.             |
| `begin_date`      | Date          | Start date of the call.(YYYY-MM-DD)                   |
| `deadline`        | Date          | Deadline for application submission.(YYYY-MM-DD)      |
| `min_advance`     | Float         | Minimum advance required for application.             |
| `min_papa`        | Float         | Minimum PAPA score required for application.          |
| `format`          | String        | Format of the call.(virtual,presencial or mixed)      |
| `year`            | Integer       | Year of the exchange.                                 |
| `semester`        | Integer       | Semester of the exchange.(1,2)                        |
| `description`     | Text          | Description of the call. May be null.                 |
| `available_slots` | Integer       | Number of available slots for the call.               |
| `note`            | Text          | Additional notes about the call.May be null           |

# 6.  Get details of close call
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/call/closed/<id>/`. The `id` is the identification of the selected call.

**Method:** `GET`

**Description:** Used to view all details of the specific close call. 

**Inputs:** NONE 

**Outputs:**

| Field Name            | Type          | Description                                      |
|----------------------|---------------|---------------------------------------------------|
|`university_name`     | String        | Name of the university offering the call.         |
| `begin_date`         | Date          | Start date of the call. (YYYY-MM-DD)              |
| `deadline`           | Date          | Deadline for application submission.(YYYY-MM-DD)  |
| `min_advance`        | Float         | Minimum advance required for application.         |
| `min_papa`           | Float         | Minimum PAPA score required for application.      |
| `format`             | String        | Format of the call(virtual,presencial or mixed).  |
| `year`               | Integer       | Year of the exchange.                             |
| `semester`           | Integer       | Semester of the exchange (1 or 2)                 |
| `description`        | Text          | Description of the call.                          |
| `available_slots`    | Integer       | Number of available slots for the call.           |
| `note`               | Text          | Additional notes about the call.                  |
| `highest_papa_winner`| Float         | Highest PAPA score among winners of the call.     |
| `minimum_papa_winner` | Float         | Minimum PAPA score among winners of the call.     |
| `selected`           | Integer       | Number of winners.                                |


# 7.  Get Call with Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/apiu/`.

**Method:** `GET`

**Description:** Return all calls with university info.

**Permissions:** Employee and Admin

**Inputs:** NONE 

**Outputs:**

| Field Name            | Type       | Description                                               |
|-----------------------|------------|-----------------------------------------------------------|
| `university_id`       | Dictionary | Dictionary                                                |
| {-`id`                | int        | University ID                                             |
| -`region`             | String     | University Region                                         |
| -`name`               | String     | University name                                           |
| -`webpage`            | String     | University webpage                                        |
| -`country`            | String     | University country                                        |
| -`city`               | String     | University city                                           |
| -`academic_offer`     | String     | University academic_offer                                 |
| -`exchange_info` }    | String     | University exchange_info                                  |
| `active`              | bool       | True if is active, false otherwise                        |
| `begin_date`          | Date       | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date       | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float      | Minimum advance required for application.                 |
| `min_papa`            | Float      | Minimum PAPA score required for application.              |
| `format`              | String     | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String     | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer    | Year of the exchange.                                     |
| `semester`            | Integer    | Semester of the exchange. (1,2)                           |
| `language`            | String     | Language of the call according to ISO 639-1               |
| `description`         | Text       | Description of the call.                                  |
| `available_slots`     | Integer    | Number of available slots for the call.                   |
| `note`                | Text       | Additional notes about the call.                          |
| `highest_papa_winner` | Float      | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float      | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer    | Number of winners.                                        |


# 7.1  Get Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/apiu/`.

**Method:** `GET`

**Description:** Return all calls.

**Permissions:** Employee and Admin

**Inputs:** NONE 

**Outputs:**

| Field Name            | Type    | Description                                               |
|-----------------------|---------|-----------------------------------------------------------|
| `university_id`       | int     | ID of the University offering the call                    |
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

# 8.  Post Call: Employee
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

| Field Name | Type | Description                         |
|------------|------|-------------------------------------|
| `mensaje`  | str  | "Convocatoria creada exitosamente"  | 
| `id`       | int  | ID of the new call                  |



# 9.  Get Call by ID: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/<int:pk>/`.

**Method:** `PUT`

**Description:** Get a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name             | Required       | Type    | Description                                                |
|------------------------|----------------|---------|------------------------------------------------------------|
| `call_id`              | YES - In Path  | int     | ID of the call to be updated.                              |


**Outputs:**

| Field Name            | Type       | Description                                               |
|-----------------------|------------|-----------------------------------------------------------|
| `id`                  | int        | ID of the call.                                           | 
| `university_id`       | Dictionary | Dictionary                                                |
| {-`id`                | int        | University ID                                             |
| -`region`             | String     | University Region                                         |
| -`name`               | String     | University name                                           |
| -`webpage`            | String     | University webpage                                        |
| -`country`            | String     | University country                                        |
| -`city`               | String     | University city                                           |
| -`academic_offer`     | String     | University academic_offer                                 |
| -`exchange_info` }    | String     | University exchange_info                                  | 
| `active`              | bool       | True if is active, false otherwise                        |
| `begin_date`          | Date       | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date       | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float      | Minimum advance required for application.                 |
| `min_papa`            | Float      | Minimum PAPA score required for application.              |
| `format`              | String     | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String     | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer    | Year of the exchange.                                     |
| `semester`            | Integer    | Semester of the exchange. (1,2)                           |
| `language`            | String     | Language of the call according to ISO 639-1               |
| `description`         | Text       | Description of the call.                                  |
| `available_slots`     | Integer    | Number of available slots for the call.                   |
| `note`                | Text       | Additional notes about the call.                          |
| `highest_papa_winner` | Float      | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float      | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer    | Number of winners.                                        |


# 10.  Update Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api_put/<int:pk>/`.

**Method:** `PUT`

**Description:** Update a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name            | Required      | Type    | Description                                               |
|-----------------------|---------------|---------|-----------------------------------------------------------|
| `call_id`             | YES - In Path | int     | ID of the call to be updated.                             |
| `university_id`       | NO            | int     | ID of the University offering the call.                   | 
| `active`              | NO*           | bool    | true if is active, false otherwise                        |
| `begin_date`          | NO            | Date    | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | NO            | Date    | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | NO            | Float   | Minimum advance required for application.                 |
| `min_papa`            | NO            | Float   | Minimum PAPA score required for application.              |
| `format`              | NO*           | String  | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | NO*           | String  | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | NO            | Integer | Year of the exchange.                                     |
| `semester`            | NO            | Integer | Semester of the exchange. (1,2)                           |
| `language`            | NO*           | String  | Language of the call according to ISO 639-1               |
| `description`         | NO            | Text    | Description of the call.                                  |
| `available_slots`     | NO            | Integer | Number of available slots for the call.                   |
| `note`                | NO            | Text    | Additional notes about the call.                          |
| `highest_papa_winner` | NO            | Float   | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | NO            | Float   | Minimum PAPA score among winners of the call.             |
| `selected`            | NO            | Integer | Number of winners.                                        |

* Please take into account the enums; incorrectly inserted enums are going to cause errors when retrieving calls.

**Outputs:**

| Field Name       | Type  | Description                                |
|------------------|-------|--------------------------------------------|
| `mensaje`        | str   | "Convocatoria actualizada exitosamente"    |


# 11.  Delete Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required       | Type | Description                        |
|----------------------|----------------|------|------------------------------------|
| `call_id`            | YES - In Path  | int  | ID of the call to be updated.      |


**Outputs:** 

| Field Name           | Type | Description                                  |
|----------------------|------|----------------------------------------------|
| `mensaje`            | str  | "Convocatoria eliminada satisfactoriamente"  |

# 12.  Open Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/opened/`.

**Method:** `GET`

**Description:** Return open calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name            | Type        | Description                                               |
|-----------------------|-------------|-----------------------------------------------------------|
| `id`                  | int         | ID of the call.                                           | 
| `university_id`       | Dictionary  | Dictionary                                                |
| {-`id`                | int         | University ID                                             |
| -`region`             | String      | University Region                                         |
| -`name`               | String      | University name                                           |
| -`webpage`            | String      | University webpage                                        |
| -`country`            | String      | University country                                        |
| -`city`               | String      | University city                                           |
| -`academic_offer`     | String      | University academic_offer                                 |
| -`exchange_info` }    | String      | University exchange_info                                  |
| `active`              | bool        | True if is active, false otherwise                        |
| `begin_date`          | Date        | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date        | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float       | Minimum advance required for application.                 |
| `min_papa`            | Float       | Minimum PAPA score required for application.              |
| `format`              | String      | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String      | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer     | Year of the exchange.                                     |
| `semester`            | Integer     | Semester of the exchange. (1,2)                           |
| `language`            | String      | Language of the call according to ISO 639-1               |
| `description`         | Text        | Description of the call.                                  |
| `available_slots`     | Integer     | Number of available slots for the call.                   |
| `note`                | Text        | Additional notes about the call.                          |
| `highest_papa_winner` | Float       | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float       | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer     | Number of winners.                                        |


# 13.  Closed Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/closed/`.

**Method:** `GET`

**Description:** Return closed calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name            | Type       | Description                                               |
|-----------------------|------------|-----------------------------------------------------------|
| `id`                  | int        | ID of the call.                                           | 
| `university_id`       | Dictionary | Dictionary                                                |
| {-`id`                | int        | University ID                                             |
| -`region`             | String     | University Region                                         |
| -`name`               | String     | University name                                           |
| -`webpage`            | String     | University webpage                                        |
| -`country`            | String     | University country                                        |
| -`city`               | String     | University city                                           |
| -`academic_offer`     | String     | University academic_offer                                 |
| -`exchange_info` }    | String     | University exchange_info                                  | 
| `active`              | bool       | True if is active, false otherwise                        |
| `begin_date`          | Date       | Calls start date.(YYYY-MM-DD)                             |
| `deadline`            | Date       | Calls deadline date for submission.(YYYY-MM-DD)           |
| `min_advance`         | Float      | Minimum advance required for application.                 |
| `min_papa`            | Float      | Minimum PAPA score required for application.              |
| `format`              | String     | Format of the call(virtual,presencial or mixed).          |
| `study_level`         | String     | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`                | Integer    | Year of the exchange.                                     |
| `semester`            | Integer    | Semester of the exchange. (1,2)                           |
| `language`            | String     | Language of the call according to ISO 639-1               |
| `description`         | Text       | Description of the call.                                  |
| `available_slots`     | Integer    | Number of available slots for the call.                   |
| `note`                | Text       | Additional notes about the call.                          |
| `highest_papa_winner` | Float      | Highest PAPA score among winners of the call.             |
| `minimum_papa_winner` | Float      | Minimum PAPA score among winners of the call.             |
| `selected`            | Integer    | Number of winners.                                        |

# 14.  Filter Over Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/employee_filter/`.

**Method:** `GET`

**Description:** Return calls filtered by if is active, university_id, university_name, deadline, format, study_level, year
        semester, region, country, language.

* Priority is given to searches with an ID. This indicates that if an ID is specified, the system will exclusively search for the call associated with that ID.

**Permissions:** Employee and Admin.

**Inputs:**

All parameters are optional, but at least, an empty dictionary {} must be send.

| Field Name        | Required      | Type                                | Description                                               |
|-------------------|---------------|-------------------------------------|-----------------------------------------------------------|
| `call_id`         | Optional      | int                                 | Call ID                                                   |
| `active`          | Optional      | String (true, false) or Python Bool | True if is active, false otherwise.                       |
| `university_id`   | Optional      | int                                 | ID of the University offering the call.                   |
| `university_name` | Optional      | String                              | Name of the University offering the call.                 |
| `deadline`        | Optional      | date                                | Calls deadline date for submission.(YYYY-MM-DD)           |
| `format`          | Optional      | String (Enum)                       | Format of the call(virtual,presencial or mixed).          |
| `study_level`     | Optional      | String (Enum)                       | Value from (pre_pregrado,pos_postgrado or doc_doctorado). |
| `year`            | Optional      | int                                 | Year of the exchange.                                     |
| `semester`        | Optional      | int                                 | Semester of the exchange. (1,2)                           |
| `region`          | Optional      | String (Enum)                       | University region.*                                       |
| `country`         | Optional      | String                              | University country.                                       |
| `language`        | Optional      | String (Enum)                       | Language that is demanded by the call.                    |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"},
    {"value": "AS", "display": "Asia"}


**Outputs:** 

| Field Name            | Type    | Description                                                   |
|-----------------------|---------|---------------------------------------------------------------|
| `id`                  | int     | ID of the call.                                               | 
| `university_id`       | dict    | Information of the University offering the call.              |
| {-`id`                | int        | University ID                                             |
| -`region`             | String     | University Region                                         |
| -`name`               | String     | University name                                           |
| -`webpage`            | String     | University webpage                                        |
| -`country`            | String     | University country                                        |
| -`city`               | String     | University city                                           |
| -`academic_offer`     | String     | University academic_offer                                 |
| -`exchange_info` }    | String     | University exchange_info                                  |
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


# 15.  Get Universities: Employee
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
    {"value": "SG", "display": "Convenio Sigueme/Nacional"},
    {"value": "AS", "display": "Asia"}

# 16.  Get University by ID: Employee
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
    {"value": "SG", "display": "Convenio Sigueme/Nacional"},
    {"value": "AS", "display": "Asia"}


# 17.  Create Universities: Employee
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

| Field Name | Type | Description                       |
|------------|------|-----------------------------------|
| `mensaje`  | str  | "Universidad creada exitosamente" | 
| `id`       | int  | New University ID                 |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"},
    {"value": "AS", "display": "Asia"}



# 18.  Update Universities: Employee
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

| Field Name        | Type        | Description                                 |
|-------------------|-------------|---------------------------------------------|
| `mensaje`         | int         | "Universidad actualizada exitosamente"      |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"},
    {"value": "AS", "display": "Asia"}


# 19.  Delete Universities: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:**

| Field Name    | Type     | Description                                  |
|---------------|----------|----------------------------------------------|
| `mensaje`     | integer  | "Universidad eliminada satisfactoriamente"   |