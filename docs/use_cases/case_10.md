# Endpoints for Case 10

## 1. Filter and Retrieve all Applicants for a Specific Call

**URL:** `application/applicants/<call_id>/`

**Method:** `GET`

**Description:** Retrieves applicants for a specific call  based on provided filters. Filters can be applied to narrow down the search criteria.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Filters:** The filters that will be allowed will be student_id and university_name.

**Inputs:** Query parameters.

| Name      | Type   | Description                                                 |
|-----------|--------|-------------------------------------------------------------|
| `filters` | Object | Dictionary containing filters for applicant data.(Optional) |
| `call_id`    | Integer | ID of the call  to retrieve applicants for.                 |

**Outputs:**

| Name                 | Type    | Description                                           |
|----------------------|---------|-------------------------------------------------------|
| `student_id`         | Integer | Unique identifier of the student.                     |
| `student_name`       | String  | Full name of the student.                             |
| `university_name`    | String  | Name of the university where the student is an applicant|
| `university_country` | String  | Country where the university is located.              |
<hr style="border:2px solid grey">


## 2. Get documents for a specific student in the specific call
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
The response will be a JSON object containing document names as keys and their corresponding public links as values.

<hr style="border:2px solid grey">

## 3.Update state documents for a specific application

**URL:** `/application/update_state_documents/<call_id>/<student_id>/`

**Method:** `PUT`

**Description:** Updates the state documents for a specific application associated with a call and a student.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** 

| Name              | Type   | Description                                    |
|-------------------|--------|------------------------------------------------|
| `state_documents` | Integer| The new state of documents for the application. This should be one of the following values: `0` (Not Reviewed), `1` (Modification Requested), or `2` (Documents Approved). |

**Outputs:**

## 4. Add Comment to Application

**URL:** `/application/add_comment/<call_id>/<student_id>/`

**Method:** `POST`

**Description:** Adds a comment to a student's application for a specific call.

**Authorization:** User authentication is required (Bearer token), and the user must be an employee.

**Inputs:** JSON object in the request body.

| Name         | Type   | Description                                   |
|--------------|--------|-----------------------------------------------|
| `comment_docs`    | String | The comment to be added to the application.  |

**Outputs:**