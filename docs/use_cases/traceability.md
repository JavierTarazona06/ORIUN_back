# Traceability

Códigos Axios: https://docs.google.com/document/d/1dAn8UFItyqq34QpMD-qJw1PwswaAh9L6zcSQaDYI02Y/edit#heading=h.986fwnir0p28

# 1. Get and Filter Trace
<span style="color: green; font-weight: bold;"> Done </span>

**URL:** `/traceability/get/`.

**Method:** `GET`

**Description:** Get all trace and/or filter them.

**Permissions:** Employee.

**Inputs:** In Path

| Field Name        | Required | Type   | Description                                              |
|-------------------|----------|--------|----------------------------------------------------------|
| `id`              | NO       | int    | id of the trace                                          |
| `view`            | NO       | string | Name of the view that was traced                         |
| `method`          | NO       | string | Name of the method that was traced (POST,GET,PUT,DELETE) |
| `user_id`         | NO       | int    | ID of the user (not C.C) that was traced                 |
| `from_date`       | NO       | string | Begin date that was traced                               |
| `until_date`      | NO       | string | Limit date that was traced                               |

**Outputs:**

| Field Name   | Type      | Description                                              |
|--------------|-----------|----------------------------------------------------------|
| `id`         | int       | id of the trace                                          |
| `time`       | timestamp | Ex. "2024-05-12T04:22:13.522458Z"                        |
| `method`     | string    | Name of the method that was traced (POST,GET,PUT,DELETE) |
| `view`       | string    | Name of the view that was traced                         |
| `given_data` | string    | More info. of teh trace                                  |
| `user_id`    | int       | ID of the user (not C.C) that was traced                 |