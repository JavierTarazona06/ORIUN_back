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

**Description:**  Used to filter and display open calls based on several criteria, such as  country, language requirement and university name. Retrieves a list of open calls based on the provided criteria.

**Inputs:**  These inputs (parameters) are not mandatory, since they are only filters. That means that you can send no filter, one filter, some of them or all of them. 


| Parameter        | Description                                      | Type      | Required | Example                                               |   
|------------------|--------------------------------------------------|-----------|----------|-------------------------------------------------------|
| `country`        | Country of the university                        | String    | No       | country=Colombia                                      |
| `language`       | Language requirement for the call                | ArrayField| No       | language=es                                           |
| `university_name`| Name of the university                           | String    | No       | name_university=Universidad%20de%20los%20Andes        |

**Outputs:**

| Name                | Type       | Description                                                  |
|---------------------|------------|--------------------------------------------------------------|
| `university_name`   | String     | Name of the university offering the call.                    |
| `country`           | String     | Country where the call is offered.                           |
| `language`          | ArrayField | Language requirement for the call.                           |
| `deadline`          | Date       | Deadline for application submission for the call.(YYYY-MM-DD)|



## 4. Endpoint filter and display closed calls
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/call/closed/`. 

**Method:** `GET`

**Description:**  Used to filter and display close calls based on several criteria, such as country, language requirement, and university name. Retrieves a list of closed calls based on the provided criteria.

**Inputs:** These inputs(paramaters) are not mandatory, since they are only filters. That means that you can send no filter, one filter, some of them or all of them. 

| Parameter         | Description                                      | Type      | Required | Example                                               |   
|-------------------|--------------------------------------------------|-----------|----------|-------------------------------------------------------|
| `country`         | Country of the university                        | String    | No       | country=Colombia                                      |
| `language `       | Language requirement for the call                | ArrayField| No       | language=es                                           |
| `university_name` | Name of the university                           | String    | No       | name_university=Universidad%20de%20los%20Andes        |

**Outputs:**
| Field Name                        | Data Type    | Description                                                      |
|-----------------------------------|--------------|------------------------------------------------------------------|
| `university_name`                 | String       | Name of the university offering the call.                        |
| `country`                         | String       | Country where the call is offered.                               |
| `language`                        | ArrayField   | Language requirement for the call.                               |
| `deadline`                        | Date         | Deadline for application submission for the call.(YYYY-MM-DD)    |
| `minimum_papa_winner`              | Float        | Minimum PAPA score among winners of the call.                    |

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


# 7.  Get Call: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/`.

**Method:** `GET`

**Description:** Return all calls.

**Permissions:** Employee and Admin

**Inputs:** NONE 

**Outputs:**

| Field Name            | Type          | Description                                               |
|----------------------|---------------|------------------------------------------------------------|
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



# 9.  Get Call by ID: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/<int:pk>/`.

**Method:** `PUT`

**Description:** Get a call according to the giving ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                |
|----------------------|---------------|---------------|------------------------------------------------------------|
|`call_id`             | YES - In Path | int           | ID of the call to be updated.                              |


**Outputs:**

| Field Name            | Type          | Description                                                |
|-----------------------|---------------|------------------------------------------------------------|
| `id`                  | int           | ID of the call.                                            | 
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


# 10.  Update Call: Employee
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


# 11.  Delete Call: Employee
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


# 12.  Open Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/opened/`.

**Method:** `GET`

**Description:** Return open calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name           | Type          | Description                                                |
|----------------------|---------------|------------------------------------------------------------|
|`id`                  | int           | ID of the call.                    | 
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


# 13.  Closed Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/closed/`.

**Method:** `GET`

**Description:** Return closed calls.

**Permissions:** Employee and Admin.

**Inputs:** None

**Outputs:** 

| Field Name           | Type          | Description                                                |
|----------------------|---------------|------------------------------------------------------------|
|`id`                  | int           | ID of the call.                    | 
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

# 14.  Filter Over Calls: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/api/employee_filter/`.

**Method:** `GET`

**Description:** Return calls filtered by if is active, university_id, university_name, deadline, format, study_level, year
        semester, region, country, language.

**Permissions:** Employee and Admin.

**Inputs:**

| Field Name           | Required      | Type           | Description                                                |
|----------------------|---------------|----------------|------------------------------------------------------------|
|`active`              | Optional      | bool           | True if is active, false otherwise.                        |
|`university_id`       | Optional      | int            | ID of the University offering the call.                    |
|`university_name`     | Optional      | String         | Name of the University offering the call.                  |
|`deadline`            | Optional      | date           | Calls deadline date for submission.(YYYY-MM-DD)            |
|`format`              | Optional      | String (Enum)  | Format of the call(virtual,presencial or mixed).           |
|`study_level`         | Optional      | String (Enum)  | Value from (pre_pregrado,pos_postgrado or doc_doctorado).  |
|`year`                | Optional      | int            | Year of the exchange.                                      |
|`semester`            | Optional      | int            | Semester of the exchange. (1,2)                            |
|`region`              | Optional      | String (Enum)  | University region.*                                        |
|`country`             | Optional      | String         | University country.                                        |
|`language`            | Optional      | String (Enum)  | Language that is demanded by the call.                     |

* University Regions:
    {"value": "NA", "display": "Norte América"},
    {"value": "LA", "display": "Latinoamérica"},
    {"value": "EU", "display": "Europa"},
    {"value": "OC", "display": "Oceanía"},
    {"value": "AN", "display": "Uniandes"},
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


**Outputs:** 

| Field Name           | Type          | Description                                                   |
|----------------------|---------------|---------------------------------------------------------------|
| `id`                 | int           | ID of the call.                                               | 
| `university_id`      | int           | ID of the University offering the call.                       | 
| `active`             | bool          | True if is active, false otherwise                            |
| `begin_date`         | Date          | Calls start date.(YYYY-MM-DD)                                 |
| `deadline`           | Date          | Calls deadline date for submission less than the given param. |
| `min_advance`        | Float         | Minimum advance required for application.                     |
| `min_papa`           | Float         | Minimum PAPA score required for application.                  |
| `format`             | String        | Format of the call(virtual,presencial or mixed).              |
| `study_level`        | String        | Value from (pre_pregrado,pos_postgrado or doc_doctorado).     |
| `year`               | Integer       | Year of the exchange.                                         |
| `semester`           | Integer       | Semester of the exchange. (1,2)                               |
| `language`           | String        | Language of the call according to ISO 639-1                   |
| `description`        | Text          | Description of the call.                                      |
| `available_slots`    | Integer       | Number of available slots for the call.                       |
| `note`               | Text          | Additional notes about the call.                              |
| `highest_papa_winner`| Float         | Highest PAPA score among winners of the call.                 |
| `minimum_papa_winner` | Float         | Minimum PAPA score among winners of the call.                 |
| `selected`           | Integer       | Number of winners.                                            |


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
    {"value": "SG", "display": "Convenio Sigueme/Nacional"}


# 16.  Create Universities: Employee
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


# 17.  Get University by ID: Employee
<span style="color: green; font-weight: bold;"> FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `PUT`

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

**Outputs:** None



# REGISTER ENDPOINTS

# . Post User Student
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None

# . Update User Student
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None

# . Read User Student
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None


# . Post User Employee
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None

# . Update User Employee
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None

# . Read User Employee
<span style="color: green; font-weight: bold;"> NOT FINISHED </span>

**URL:** `/call/university_api/<int:pk>/`.

**Method:** `DELETE`

**Description:** Delete a university according to the given ID.

**Permissions:** Employee and Admin.

**Inputs:** 

| Field Name           | Required      | Type          | Description                                                  |
|----------------------|---------------|---------------|--------------------------------------------------------------|
| `id`                 | YES - In Path | integer       | A unique integer value identifying this university.          |

**Outputs:** None



# 20. Check if student is eligible for an application
**URL:** `student/eligible/`

**Method:** `GET`

**Description:** Used to know if a student can apply to a call or not. If not, the endpoint will tell you the reason (therefor you can just show it to the student). So, if the `eligibility` is `false` then you should show the user the message, if it is `true` then the user can continue the process (applying to a call).

**Authorization:** the bearer token of the user 

**Inputs:** query params 

| Name       | Type    | Description                                |
|------------|---------|--------------------------------------------|
| `call`     | Integer | ID of the call the student wants to apply. |

**Outputs:**

| Name          | Type    | Description                                                                                                                      |
|---------------|---------|----------------------------------------------------------------------------------------------------------------------------------|
| `eligibility` | Boolean | True if the user can apply to the call (therefor can continue) or False otherwise.                                               |
| `message`     | String  | Let's the user know the reason of not being able to apply to the call (in other words, when `elibility` is `true` this is empty. |


# 21. Get initial information about the student
**URL:** `student/info-application/`

**Method:** `GET`

**Description:** Used to know initial information that will be used into the application, such as the contact person information, medicines or diseases the student might have, also the information of their coordinator.

**Authorization:** the bearer token of the user 

**Inputs:** None

**Outputs:**

| Name               | Type   | Description                                                                                                                                               |
|--------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `contact_person`   | JSON   | Information of the contact person for the student. It might be `null`, in that case it means the student does not have any information in this field yet. |
| `diseases`         | String | Diseases the student might have, it can also be `null`, if so it indicates that the user does not have a disease or it has not been set.                  |
| `medication`       | String | Medication the student might take, it can also be `null`, if so it indicates that the user does not take any medication or it has not been set.           |
| `info_coordinator` | JSON   | Information about the coordinator of the student, this is where they will send the documents so they can be signed.                                       |

`contact_person`:

| Name           | Type    | Description                                                      |
|----------------|---------|------------------------------------------------------------------|
| `id`           | Integer | Identifier of the contact person, do not show it to the student. |
| `name`         | String  | Name of the contact person                                       |
| `last_name`    | String  | Last name of the contact person                                  |
| `email`        | String  | Email of the contact person                                      |
| `relationship` | String  | Relationship of the contact person                               |
| `cellphone`    | String  | Cellphone of the contact person                                  |

`info_coordinator`:

| Name                             | Type   | Description                              |
|----------------------------------|--------|------------------------------------------|
| `Coordinador Curricular`         | String | Name of the curricular coordinator.      |
| `Teléfono Coordinador`           | String | Telephone of the curricular coordinator. |
| `Correo Coordinador`             | String | Email of the curricular coordinator.     |
| `Correo Coordinación Curricular` | String | Name of the curricular coordination.     |


# 22. Get region of the call
**URL:** `application/region_call/`

**Method:** `GET`

**Description:** Used to know the region of the call, this is used to know which docs will be needed and therefor which interface must be presented to the student.

**Authorization:** the bearer token of the user 

**Inputs:** query params 

| Name       | Type    | Description                                |
|------------|---------|--------------------------------------------|
| `call`     | Integer | ID of the call the student wants to apply. |

**Outputs:**

| Name     | Type   | Description                                                                                      |
|----------|--------|--------------------------------------------------------------------------------------------------|
| `region` | String | Region of the call. There are 3 possibles strings: `Uniandes`, `Nacional`, and `Internacional` . |

<hr style="border:2px solid gray">

Which information should the student give?

## Informacion de contacto
- Nombre
- Apellido
- Email
- Relacion (que relacion tiene con el estudiante)
- Telefono

## Informacion de salud
- Enfermedades
- Medicamentos

## Informacion Institucion de destino
- Nombre facultad de destino
- Nombre programa de destino
- Nombre del contacto en la institucion
- Cargo del contacto en la institucion
- Telefono del contacto en la institucion
- Correo del contacto en la institucion

## Informacion movilidad
- Fecha de inicio
- Fecha de finalizacion

## Informacion de los cursos
- Codigo UNAL, Nombre UNAL, codigo destino, nombre destino

<hr style="border:2px solid gray">

These are the documents that all student must submit (base case):
- Formato de solicitud
- Formato de responsabilidad nacional
- Tratamiento de datos personales
- Documento de identidad
- Certificado de notas
- Otros documentos (here the student can upload any document that the university might require)

What types of regions are there and what should be display for each one?
1. Uniandes:
    - Same as the base case
2. Internacional:
    - Carta de motivacion
    - Pasaporte
    - Certificado del idioma
    - Carta demostrando suficiencia economica
3. Nacional:
    - Documento 'sigueme' 
    - Cerficicado de matricula
    - Cerficicado afiliacion EPS 
    - Carta demostrando suficiencia economica

Which documents can only have a submit button?
- Documento de identidad
- Certificado de notas
- Otros documentos (here the student can upload any document that the university might require)
- Carta de motivacion
- Certificado del idioma
- Carta demostrando suficiencia economica
- Certificado de matricula
- Certificado afiliacion EPS
