## 1.  Endpoint to Retrieve all Applications with Corresponding Results for Employees

**URL:** `application/results_employee/<int:call_id>/`

**Method:** `GET`

**Description:**  Endpoint to retrieve all applications with corresponding results, indicating whether each application has been accepted or not.

**Authorization:** User authentication is required (Bearer token), and the user must have `IsEmployee` permissions.


**Inputs:** 

### URL Parameters:
- `call_id` (int): The ID of the call for which the applications are being retrieved.

### Query Parameters:
- `approved` (boolean, optional): Filter to retrieve applications based on their approval status.
- `student_id` (int, optional): Unique identifier of the student.
- Any additional query parameters to filter applications.


**Outputs:**

| Name                 | Type    | Description                                              |
|----------------------|---------|----------------------------------------------------------|
| `student_id`         | Integer | Unique identifier of the student.                        |
| `student_name`       | String  | Full name of the student.                                |
| `university_name`    | String  | Name of the university where the student is an applicant.|
| `university_country` | String  | Country where the university is located.                 |
| `call`               | Integer | Unique identifier of the call.                           |
| `approved`           | Boolean | Approval status of the application.                      |

## 2.  Endpoint to Retrieve Application Results for Students

**URL:** `application/results/<int:call_id>/`

**Method:** `GET`

**Description:** Endpoint to retrieve the result of a student's application, indicating whether the application has been accepted, not accepted, or is pending verification.

**Authorization:** User authentication is required (Bearer token), and the user must have `IsStudent` permissions.

**Inputs:**

### URL Parameters:
- `call_id` (int): The ID of the call for which the application result is being retrieved.

### Query Parameters:
None

**Outputs:**

| Name                 | Type    | Description                                              |
|----------------------|---------|----------------------------------------------------------|
| `message`            | String  | Message indicating the result of the application.        |
| `call`               | Integer | Unique identifier of the call.                           |
| `university_name`    | String  | Name of the university where the student is an applicant.|
| `university_country` | String  | Country where the university is located.                 |
| `state_documents`    | Integer | Status of the documents (e.g., modified, not reviewed, accepted).|
| `approved`           | Boolean | Approval status of the application.                      |
| `call_description`   | String  | Description of the call.                                 |
| `student_id`         | Integer | Unique identifier of the student.                        |


# 3. Endpoint to Retrieve Student's Applications


**URL:** `application/student/`

**Method:** `GET`

**Description:** Used to get all the applications the student has, and their status.

**Authorization:** User authentication is required (Bearer token),  and the user must have `IsStudent` permissions.

**Inputs:** None

**Outputs:**

| Name                 | Type    | Description                                              |
|----------------------|---------|----------------------------------------------------------|
| `student_id`         | Integer | Unique identifier of the student.                        |
| `call`               | Integer | Unique identifier of the call.                           |
| `university_name`    | String  | Name of the university where the student is an applicant.|
| `university_country` | String  | Country where the university is located.                 |
| `result_state`       | String  | State of the application result (e.g., 'Aceptado', 'No aceptado', 'Pendiente de revisión', 'Modificación solicitada a documentación'). |
| `call_description`   | String  | Description of the call.                                 |
| `approved`           | Boolean | Approval status of the application.                      |