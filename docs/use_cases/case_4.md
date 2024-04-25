# Endpoints for Case 4

## 1. Check if student is eligible for an application

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
| `eligibility` | Boolean | true if the user can apply to the call (therefor can continue) or false otherwise.                                               |
| `message`     | String  | Let's the user know the reason of not being able to apply to the call (in other words, when `elibility` is `true` this is empty. |

<hr style="border:2px solid gray">

## 2. Get initial information about the student

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

<hr style="border:2px solid gray">

## 3. Get region of the call

**URL:** `application/region_call/`

**Method:** `GET`

**Description:** Used to know the region of the call, this is used to know which docs will be needed and therefor which interface must be presented to the student. At the end of file is the list with the names of each possible file in each region.

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

## 4. Check contact person and create documents

**URL:** `application/create_forms/`

**Method:** `POST`

**Description:** It checks whether the user has a contact person or not (you should also do this in the frontend), and if this is true then the filled documents will be created (the documents with the initial information of the student given in the registration and the form).

**Authorization:** the bearer token of the user 

**Inputs:** body

| Name             | Type          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `medication`     | String        | Medication the student might take, it can be an empty string (which means the student does not take any medication). It is not obligatory.                                                                                                                                                                                                                                                                                                                                  |
| `diseases`       | String        | Diseases the student might have, it can be an empty string (which means the student does not have any disease). It is not obligatory.                                                                                                                                                                                                                                                                                                                                       |
| `contact_person` | JSON          | Information of the contact person of the student. You must send all the values in the JSON (if you decide to send it) or the contact_person must be known before hand (part of the output of the second endpoint), that's why you must check that these fields (in the frontend) are not empty. In the second case (info was known before) do not send anything. |
| `call`           | Integer       | ID of the call the student wants to apply. It is obligatory.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `info_mobility`  | JSON          | Basic information about the mobility that is not in the call model. If the student doesn't put any information, do not send an empty string. It is not obligatory.                                                                                                                                                                                                                                                                                                          |
| `info_courses`   | List of JSONs | Information about the courses the student wants to take. If the student doesn't put any information, do not send an empty string. It is not obligatory.                                                                                                                                                                                                                                                                                                                     |

**Outputs:**

| Name      | Type   | Description                                                                             |
|-----------|--------|-----------------------------------------------------------------------------------------|
| `message` | String | Let's you know the documents are ready with a message like "Forms filled successfully". |

**Exceptions:**

If you do not send the info and there was no contact_person set before, the app will send you a 400 status, with a message that says "La persona de contacto no ha sido definida".

`contact_person`:

| Name           | Type    | Description                                                      |
|----------------|---------|------------------------------------------------------------------|
| `name`         | String  | Name of the contact person                                       |
| `last_name`    | String  | Last name of the contact person                                  |
| `email`        | String  | Email of the contact person                                      |
| `relationship` | String  | Relationship of the contact person                               |
| `cellphone`    | String  | Cellphone of the contact person                                  |

`info_mobility`:

| Name                  | Type   | Description                                                    |
|-----------------------|--------|----------------------------------------------------------------|
| `start_date`          | String | Starting date of the call, the format must be "day-month-year" |
| `end_date`            | String | Ending date of the call, the format must be "day-month-year"   |
| `dest_faculty`        | String | Name of the faculty in the destination university              |
| `dest_program`        | String | Name of the program in the destination university              |
| `dest_contact_name`   | String | Name of the contact person in the destination university       |
| `dest_contact_charge` | String | Charge of the contact person in the destination university     |
| `dest_contact_phone`  | String | Phone of the contact person in the destination university      |
| `dest_contact_email`  | String | Email of the contact person in the destination university      |

`info_courses`:

| Name           | Type   | Description                                      |
|----------------|--------|--------------------------------------------------|
| `code_unal`    | String | Code of the course in UNAL                       |
| `name_unal`    | String | Name of the course in UNAL                       |
| `code_destiny` | String | Code of the course in hte destination university |
| `name_destiny` | String | Name of the course in hte destination university |

<hr style="border:2px solid gray">

## 5. Get a document

**URL:** `application/download/`

**Method:** `GET`

**Description:** Returns a public link that can be used during 15 minutos to download the requested document.

**Authorization:** the bearer token of the user 

**Inputs:** query params 

| Name        | Type    | Description                                                                                                                                                              |
|-------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `call`      | Integer | ID of the call the student wants to apply.                                                                                                                               |
| `type_file` | String  | If the student wants to download the filled document or the original documents. If it is the first case, then it must be equal to `filled_doc` otherwise `original_doc`. |
| `name_file` | String  | Name of the document the student wants to download. Each document has an specific name, this information is at the end of the document.                                  |

**Outputs:**
    
| Name   | Type   | Description                                            |
|--------|--------|--------------------------------------------------------|
| `link` | String | Public link that can be used to download the document. |

**Exceptions:**

If the file is not found you will get a 404 status and a message "form not found". 

<hr style="border:2px solid gray">

## 6. Upload a document

**URL:** `application/upload/`

**Method:** `POST`

**Description:** Lets the user upload any document.

**Authorization:** the bearer token of the user 

**Inputs:** body 

| Name        | Type    | Description                                                                                                                             |
|-------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `call`      | Integer | ID of the call the student wants to apply.                                                                                              |
| `document`  | File    | Document the user wants to upload.                                                                                                      |
| `name_file` | String  | Name of the document the student wants to download. Each document has an specific name, this information is at the end of the document. |

**Outputs:**
    
| Name      | Type   | Description                                                                                       |
|-----------|--------|---------------------------------------------------------------------------------------------------|
| `message` | String | Let's you know the documents has been uploaded with a message like "File uploaded successfully!". |

**Exceptions:**

If the file is greater than 9MB, the API returns a 403 and message indicating that the file is too big.

**Example:** These are some examples in different languages:

```javascript
// NodeJS - Axios
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
let data = new FormData();
data.append('name', 'request_form');
data.append('document', fs.createReadStream('/home/valeria/Downloads/video.mov'));
data.append('call', '1');

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'http://localhost:8000/application/upload/',
  headers: { 
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTkxNDExLCJpYXQiOjE3MTM5ODQyMTEsImp0aSI6Ijc2MzIzNGFkNTU5NjQ4Yjc5ZTIxN2M2YzAyNjY0NjMwIiwidXNlcl9pZCI6MX0.6Hs0nCdZuZGLKl8pZ-ZjnrT5mCUUU_UxzJTkJ1K_jyA', 
    ...data.getHeaders()
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

```javascript
// Javascript - Fetch
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTkxNDExLCJpYXQiOjE3MTM5ODQyMTEsImp0aSI6Ijc2MzIzNGFkNTU5NjQ4Yjc5ZTIxN2M2YzAyNjY0NjMwIiwidXNlcl9pZCI6MX0.6Hs0nCdZuZGLKl8pZ-ZjnrT5mCUUU_UxzJTkJ1K_jyA");

const formdata = new FormData();
formdata.append("name", "request_form");
formdata.append("document", fileInput.files[0], "video.mov");
formdata.append("call", "1");

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: formdata,
  redirect: "follow"
};

fetch("http://localhost:8000/application/upload/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```
<hr style="border:2px solid gray">

## 7. Submit an application

**URL:** `application/submit/`

**Method:** `POST`

**Description:** Used to create an application. Used after the user has uploaded all the info.

**Authorization:** the bearer token of the user 

**Inputs:** body

| Name           | Type    | Description                                                                         |
|----------------|---------|-------------------------------------------------------------------------------------|
| `call`         | Integer | ID of the call the student wants to apply.                                          |
| `is_extension` | Boolean | `true` if the application is an extension of a current mobility, `false` otherwise. |

**Outputs:**
    
| Name      | Type   | Description                                                                        |
|-----------|--------|------------------------------------------------------------------------------------|
| `message` | String | Let's you know that everything went fine with a message like "Application created" |

**Exceptions:**

If there is one or more missing files, you will receive a 404 status, and a message that says which files are not yet on GCP. And a 400 if the call is closed.

<hr style="border:2px solid gray">

Which information should the student give?

### Informacion de contacto
- Nombre
- Apellido
- Email
- Relacion (que relacion tiene con el estudiante)
- Telefono

### Informacion de salud
- Enfermedades
- Medicamentos

### Informacion Institucion de destino
- Nombre facultado de destino
- Nombre programa de destino
- Nombre del contacto en la institucion
- Cargo del contacto en la institucion
- Telefono del contacto en la institucion
- Correo del contacto en la institucion

### Informacion movilidad
- Fecha de inicio (dia-mes-año)
- Fecha de finalizacion (dia-mes-año)

### Informacion de los cursos (seria una lista en la cual la persona puede meter mas de uno)
- Codigo UNAL, Nombre UNAL, codigo destino, nombre destino

<hr style="border:2px solid gray">

These are the documents that all student must submit (base case), in parentheses are the name of those files that you must used when sending them to the API:
- Formato de solicitud (request_form)
- Formato de responsabilidad nacional (responsibility_form)
- Tratamiento de datos personales (data_processing_form)
- Documento de identidad (doc_id_student)
- Certificado de notas (grades_certificate)

What types of regions are there and what should be display for each one?
1. Uniandes:
    - Same as the base case
2. Internacional:
    - Carta de motivacion (motivation_letter)
    - Pasaporte (passport)
    - Certificado del idioma (language_certificate)
    - Carta demostrando suficiencia economica (economic_letter)
3. Nacional:
    - Documento 'sigueme' (sigueme_form)
    - Certificado de matricula (payment_tuition)
    - Certificado afiliacion EPS (eps_certificate)
    - Carta demostrando suficiencia economica (economic_letter)

Which documents can only have a submit button?
- Documento de identidad
- Certificado de notas
- Carta de motivacion
- Pasaporte
- Certificado del idioma
- Carta demostrando suficiencia economica
- Certificado de matricula
- Certificado afiliacion EPS

<hr style="border:2px solid gray">

Workflow:

1. Vas a llamar el endpoint 1 (Check if student is eligible for an application) y segun eso habran dos opciones:

   1.1: `eligibility` es falso, por ende le muestras esa vista del error y en el mensaje pones lo que se retorno de `message`.

   1.2: `eligibility` es verdadero, por ende puedes seguir con el paso 2
2. Vas a llamar al endpoint 2 (Get initial information about the student), segun los datos que te retorne, vas a llenar la informacion de contacto o la informacion de salud.
3. Dependiendo de cual de los 2 botones de continuar de click la persona, el siguiente paso sera diferente. (Imagina que la caja negra es un boton :v)
3.1. La persona ya tiene sus documentos listos, por ende sigue al paso 4.
3.2 La persona quiere llenar los datos para poder obtener los formularios, entonces el usuario llenará el resto de datos, y una vez de click en continuar revisaras que la informacion de contacto este llena, bien sea por que yo te pase ese dato en el anterior endpoint o porque la persona lo lleno. Llamaras al endpoint 4 (Check contact person and create documents) y si todo esta bien, sigues con el paso 4.
4. Llamaras  al endpoint 5 (Get region of the call) y segun la region que te arroje tendras una vista diferente en el siguiente paso (que puedes ver Canva para tener una idea de como es). Además, parte del endpoint 2 te dara la informacion de la coordinacion curricular, eso lo debes incluir en esa siguiente vista, pues ahi sera a donde los estudiantes envien algunos de esos documentos.
5. El estudiante quiere descargar un documento ya llenado, o el original, para eso utilizaras el endpoint 5.
6. El estudiante sube un archivo, puedes usar el endpoint 6.
7. Ya se va a enviar todos los datos para ello esta el endpoint 7. Si son correctos los datos se le muestra la confirmacion, si no, dependiendo del error se le permite subir otros documentos o se le saca de la pantalla. Recuerda para este agregar algun boton que indique que si la aplicacion es una extension de una convocatoria en la que ya esta el estudiante, es solo un boton de verdadero o falso, pues eso lo requirere el endpoint.

![img.png](img/case_4a.png)
![img.png](img/case_4b.png)
