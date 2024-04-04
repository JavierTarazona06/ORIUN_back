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

**URL:** `/calls/open/`. 

**Method:** `GET`

**Description:**  Used to filter and display open calls based on several criteria, such as ID, region, country, language requirement, application deadline and university name.

**Inputs:** Optional 
| Parameter Name   | Type   | Description                                          |
|------------------|--------|------------------------------------------------------|
| `country`        | String | Country where the call is offered.                   |
| `language`       | String | Language requirement for the call.                   |
| `name_university`| String | Name of the university offering the call.            |

**Outputs:**

| Name                | Type   | Description                                              |
|---------------------|--------|----------------------------------------------------------|
| `name_university`   | String | Name of the university offering the call.                |
| `country`           | String | Country where the call is offered.                       |
| `language`          | String | Language requirement for the call.                       |
| `deadline`          | Date   | Deadline for application submission for the call.        |

## 4. Endpoint filter and display closed calls
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/calls/closed/`. 

**Method:** `GET`

**Description:**  Used to filter and display close calls based on several criteria, such as ID, region, country, language requirement, application deadline, university name and average of selected participant.

**Inputs:** Optional

| Parameter Name   | Type   | Description                                          |
|------------------|--------|------------------------------------------------------| 
| `country`        | String | Country where the call is offered.                   |
| `language`       | String | Language requirement for the call.                   |
| `name_university`| String | Name of the university offering the call.            |

**Outputs:**
| Field Name                        | Data Type    | Description                                                      |
|-----------------------------------|--------------|------------------------------------------------------------------|
| `name_university`                 | String       | Name of the university offering the call.                        |
| `country`                         | String       | Country where the call is offered.                               |
| `language`                        | String       | Language requirement for the call.                               |
| `deadline`                        | Date         | Deadline for application submission for the call.                |
| `average_winning_participants`    | Decimal      | Average number of selected participants (only for closed calls). |

# 5.  Get details of open call
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/calls/open/<id>/`.  The `id` is the identification of the selected call.

**Method:** `GET`

**Description:**  Used to view all the details of the selected open calls for proposals.

**Inputs:** None

**Outputs:**
| Field Name        | Type          | Description                                           |
|-------------------|---------------|-------------------------------------------------------|
|`university_name`  | Integer       | Name of the university offering the call.             |
| `begin_date`      |  Date         | Start date of the call.                               |
| `deadline`        | Date          | Deadline for application submission.                  |
| `min_advance`     | Integer       | Minimum advance required for application.             |
| `min_papa`        | Integer       | Minimum Papa score required for application.          |
| `format`          | String        | Format of the call.(virtual,presencial or mixed)      |
| `year`            | Integer       | Year of the call.                                     |
| `semester`        | Integer       | Semester of the call.                                 |
| `description`     | Text          | Description of the call. May be null.                 |
| `available_slots` | Integer       | Number of available slots for the call.               |
| `note`            | Text          | Additional notes about the call.                      |

# 6.  Get details of close call
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `/calls/closed/<id>/`. The `id` is the identification of the selected call.

**Method:** `GET`

**Description:**  Used to view all the details of the selected closed calls for proposals.

**Inputs:** NONE 

**Outputs:**
| Field Name            | Type          | Description                                      |
|----------------------|---------------|---------------------------------------------------|
|`university_name`     | Integer       | Name of the university offering the call.         |
| `begin_date`         |  Date         | Start date of the call.                           |
| `deadline`           | Date          | Deadline for application submission.              |
| `min_advance`        | Integer       | Minimum advance required for application.         |
| `min_papa`           | Integer       | Minimum Papa score required for application.      |
| `format`             | String        | Format of the call(virtual,presencial or mixed).  |
| `year`               | Integer       | Year of the call.                                 |
| `semester`           | Integer       | Semester of the call.                             |
| `description`        | Text          | Description of the call.                          |
| `available_slots`    | Integer       | Number of available slots for the call.           |
| `note`               | Text          | Additional notes about the call.                  |
| `highest_PAPA_winner`| Decimal       | Highest PAPA score among winners of the call.     |
| `minium_PAPA_winner` | Decimal       | Minimum PAPA score among winners of the call.     |
| `selected`           | Integer       | Number of winners.                                |
