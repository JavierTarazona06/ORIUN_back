# Endpoints for Case 10

## 1. Filter and Retrieve all Applicants for a Specific Call

**URL:** `application/applicants/<call_id>/`

**Method:** `GET`

**Description:** Retrieves applicants for a specific call  based on provided filters. Filters can be applied to narrow down the search criteria.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Filters:** The filters that will be allowed will be `student_id` or `state_documents`.

**Inputs:** Query parameters.

| Name              | Type    | Description                                 |
|-------------------|---------|---------------------------------------------|
| `student_id`      | Integer | Unique identifier of the student.           |
| `call_id`         | Integer | ID of the call  to retrieve applicants for. |
| `state_documents` | Integer | Status of documents that are between, modified, not reviewed, and accepted.         |

**Outputs:**

| Name                 | Type    | Description                                              |
|----------------------|---------|----------------------------------------------------------|
| `student_id`         | Integer | Unique identifier of the student.                        |
| `student_name`       | String  | Full name of the student.                                |
| `university_name`    | String  | Name of the university where the student is an applicant |
| `university_country` | String  | Country where the university is located.                 |
| `call`               | Integer | Unique identifier of the  call.                          |

<hr style="border:2px solid grey">

## 2.  Retrieve Student Information Related to an Application
**URL:** `application/<int:call_id>/<int:student_id>/student-info/`

**Method:** `GET`

**Description:** Retrieves information about a student related to an application.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** 

| Name         | Type    | Description                                    |
|--------------|---------|------------------------------------------------|
| `call_id`    | Integer | ID of the call to retrieve documents for.      |
| `student_id` | Integer | ID of the student to retrieve documents for.   |

**Outputs:**

| Name                 | Type    | Description                                              |
|----------------------|---------|----------------------------------------------------------|
| `student_id`         | Integer | Unique identifier of the student.                        |
| `student_name`       | String  | Full name of the student.                                |
| `university_name`    | String  | Name of the university where the student is an applicant |
| `university_country` | String  | Country where the university is located.                 |
| `student_major`      | String  | Major of the student.                                    |
| `call`               | Integer | Unique identifier of the  call.                          |

## 3. Get documents for a specific student in the specific call
**URL:** `application/applicants/<call_id>/documents/<student_id>/`

**Method:** `GET`

**Description:** Retrieves documents associated with a student's application for a specific call.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** Query parameters.

| Name         | Type    | Description                                    |
|--------------|---------|------------------------------------------------|
| `call_id`    | Integer | ID of the call to retrieve documents for.      |
| `student_id` | Integer | ID of the student to retrieve documents for.   |

**Outputs:**
The response will be a JSON object containing document names as keys and their corresponding public links as values, the documents vary according to region, as shown below:

 **Uniandes:**

| Name                   | Type  | Description                                    |
|------------------------|-------|------------------------------------------------|
| `request_form`         | link  | Request Form.                                  |
| `responsibility_form`  | Link  | National Responsibility Form.                  |
| `data_processing_form` | Link  | Data Processing Form.                          |
| `doc_id_student`       | Link  | Identity Document.                             |
| `grades_certificate`   | Link  | Grades Certificate.                            |

### National:

| Name                   | Type | Description                                    |
|------------------------|------|------------------------------------------------|
| `request_form`         | Link | Request Form.                                  |
| `responsibility_form`  | Link | National Responsibility Form.                  |
| `data_processing_form` | Link | Data Processing Form.                          |
| `doc_id_student`       | Link | Identity Document.                             |
| `grades_certificate`   | link | Grades Certificate.                            |
| `sigueme_form`         | link | 'Sigueme' Document.                            |
| `payment_tuition`      | link | Tuition Payment Certificate.                   |
| `eps_certificate`      | File | EPS Affiliation Certificate.                   |
| `economic_letter`      | link | Economic Sufficiency Letter.                   |

### International:
| Name                   | Type | Description                                    |
|------------------------|------|------------------------------------------------|
| `request_form`         | link | Request Form.                                  |
| `responsibility_form`  | link | National Responsibility Form.                  |
| `data_processing_form` | link | Data Processing Form.                          |
| `doc_id_student`       | link | Identity Document.                             |
| `grades_certificate`   | link | Grades Certificate.                            |
| `motivation_letter`    | link | Motivation Letter.                             |
| `passport`             | link | Passport.                                      |
| `language_certificate` | link | Language Certificate.                          |
| `economic_letter`      | link | Economic Sufficiency Letter.                   |

<hr style="border:2px solid grey">

## 4. Request a modification for an application

**URL:** `application/<int:call_id>/<int:student_id>/modify/`

**Method:** `PUT`

**Description:**  Modifies an existing application for a specific student in a specific call.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** 

| Name         | Type    | Description                                    |
|--------------|---------|------------------------------------------------|
| `call_id`    | Integer | ID of the call to retrieve documents for.      |
| `student_id` | Integer | ID of the student to retrieve documents for.   |


**Outputs:**

| Name      | Type   | Description                                                              |
|-----------|--------|--------------------------------------------------------------------------|
| `message` | String | Message indicating the application data requested to be modified, like: 'request a modification' |



## 5. Endpoint to Accept Documents for a Specific Student's Application

*URL:** `application/<int:call_id>/<int:student_id>/modify/`

**Method:** `PUT`

**Description:**  Modifies an existing application for a specific student in a specific call.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** 

| Name         | Type    | Description                                    |
|--------------|---------|------------------------------------------------|
| `call_id`    | Integer | ID of the call to retrieve documents for.      |
| `student_id` | Integer | ID of the student to retrieve documents for.   |


**Outputs:**

| Name      | Type   | Description                                                                                  |
|-----------|--------|----------------------------------------------------------------------------------------------|
| `message` | String | Message indicating the application data requested to be accepted, like: 'accepted documents' |





## 6. Add Comment to Application

**URL:** `/application/add_comment/<call_id>/<student_id>/`

**Method:** `POST`

**Description:** Adds a comment to a student's application for a specific call.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** JSON object in the request body.

| Name         | Type   | Description                                   |
|--------------|--------|-----------------------------------------------|
| `comment_docs`    | String | The comment to be added to the application.  |

**Outputs:**

| Name      | Type   | Description                                             |
|-----------|--------|---------------------------------------------------------|
| `message` | String | Message indicating that the comment has been created successfully |