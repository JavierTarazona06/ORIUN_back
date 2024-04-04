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


## 3. Endpoint calls
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `calls/{type}/`. The `type` can be `inactive` or `active`, depending on whether the user wants
to get inactive calls or active calls.

**Method:** `GET`

**Description:** Used to get all the inactive or active calls.

**Inputs:** These inputs are not mandatory, since they are only filters. That means that you can send
no filter, one filter, some of them or all of them. **COMPLETE**

| Name      | Type   | Description                               |
|-----------|--------|-------------------------------------------|
| `country` | String | Country where the call will be developed. |

**Outputs:**

| Name         | Type   | Description                               |
|--------------|--------|-------------------------------------------|
| `university` | String | Name of the university offering the call. |


## 4. Endpoint specific call
<span style="color: red; font-weight: bold;"> STATUS: NOT FINISHED </span>

**URL:** `calls/{type}/{id}/`. The `type` can be `inactive` or `active`, depending on whether the user 
wants to get inactive calls or active calls; and the `id` is the identification of the selected call.

**Method:** `GET`

**Description:** Used to info about a specific active or inactive call.

**Inputs:** None

**Outputs:**

| Name         | Type   | Description                               |
|--------------|--------|-------------------------------------------|
| `university` | String | Name of the university offering the call. |

