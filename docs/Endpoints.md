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
| `Avg_PAPA_winning_participants`   | Float        | Average number of selected participants.                         |

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
| `year`            | Integer       | Year of the call.                                     |
| `semester`        | Integer       | Semester of the call.(1,2)                            |
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
| `year`               | Integer       | Year of the call.                                 |
| `semester`           | Integer       | Semester of the call.1,2)                         |
| `description`        | Text          | Description of the call.                          |
| `available_slots`    | Integer       | Number of available slots for the call.           |
| `note`               | Text          | Additional notes about the call.                  |
| `highest_PAPA_winner`| Float         | Highest PAPA score among winners of the call.     |
| `minium_PAPA_winner` | Float         | Minimum PAPA score among winners of the call.     |
| `selected`           | Integer       | Number of winners.                                |
