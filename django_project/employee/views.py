import pytz

from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, EmployeeGetSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from .models import Employee
from django.http import JsonResponse
from rest_framework import status, permissions
from .permissions import IsEmployee
from data.constants import Constants
from traceability.models import Traceability

from data import helpers

HOUR_COL = helpers.get_col_time()

class PostUserEmployee(APIView):
    permission_classes = []
    serializer = EmployeeSerializer()

    def post(self, request):
        input_params = request.data
        username = input_params["email"]
        try:
            if not "@unal.edu.co" in input_params["email"]:
                raise ValueError("El correo no es dominio @unal.edu.co")

            # Data Validation -----
            input_params = dict(input_params)
            for key, value in input_params.items():
                if str(type(value)) == "<class 'datetime.date'>":
                    input_params[key] = value.strftime("%Y-%m-%d")
                if str(type(value)) == "<class 'int'>":
                    input_params[key] = str(value)
                else:
                    if isinstance(value, list):
                        input_params[key] = value[0]
                    else:
                        input_params[key] = value

            flag = False
            for mail in Constants.EMPLOYEES_MAILS['ORI']:
                if mail == input_params["email"] and input_params["dependency"] == 'ORI':
                    flag = True
                    break
            if not flag:
                for mail in Constants.EMPLOYEES_MAILS['DRE']:
                    if mail == input_params["email"] and input_params["dependency"] == 'DRE':
                        flag = True
                        break
            if not flag:
                raise ValueError("El correo ingresado no corresponde a un funcionario de la ORI/DRE o ingresó mal la dependencia")

            # Creating User -----
            input_params['username'] = input_params["email"]
            user = User.objects.create_user(
                username=input_params['username'],
                email=input_params['email'],
                password=input_params['password'],
                first_name=input_params['first_name'],
                last_name=input_params['last_name'],
            )
            input_params["user"] = user.id
            del input_params["username"]
            del input_params["email"]
            del input_params["password"]
            del input_params["first_name"]
            del input_params["last_name"]

            # Verification Code -----
            if "verif_code" not in input_params:
                raise ValueError("No se envío el código de verificación enviado al correo")
            else:
                verif_code_sent = input_params["verif_code"]
                del input_params["verif_code"]
                code_file_name = r"data/{}_verif_code.txt".format(input_params["id"])
                with open(code_file_name, "r") as file:
                    code_stored = file.read()
                if not (code_stored == verif_code_sent):
                    raise ValidationError(
                        "El código de verificación de acceso enviado al correo no concuerda con el ingresado")

            # Validation Serializer -----
            serializer = EmployeeSerializer(data=input_params)
            if not serializer.is_valid():
                errors = serializer.errors
                raise ValueError(str(errors))
            input_params["user"] = user

            # Create Employee -----
            Employee.objects.create(**input_params)

            this_employee = Employee.objects.get(id=input_params['id'])
            this_user = this_employee.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": str(self.__class__.__name__),
                "given_data": f"Se creó el empleado con id: {this_employee.id} y correo {this_employee.user.email}. ID de usuario: {this_employee.user.id}",
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse({'mensaje': 'Funcionario creado exitosamente'}, status=status.HTTP_200_OK)
        except Exception as e:
            try:
                user_inst = User.objects.get(username=username)
            except User.DoesNotExist:
                pass
            else:
                user_inst.delete()
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ReadUserEmployee(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def get(self, request, pk):
        try:
            myEmployee = Employee.objects.get(pk=pk)
            if not (request.user.email == myEmployee.user.email):
                raise ValidationError("El usuario {} no tiene permiso para ver la información del usuario solicitado".format(request.user))
            my_employee_qset = Employee.objects.filter(pk=pk)
            my_employee_sr = EmployeeGetSerializer(my_employee_qset, many=True).data[0]

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": str(self.__class__.__name__),
                "given_data": f"El usuario solicitó la información del emploeado con id {myEmployee.id}."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse(my_employee_sr, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserEmployee(APIView):
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def delete(self, request, pk):
        try:
            myEmployee = Employee.objects.get(pk=pk)
            ide = myEmployee.id
            myEmployee.delete()

            this_user = request.user
            data_trace = {
                "user": this_user,
                "time": HOUR_COL,
                "method": request.method,
                "view": str(self.__class__.__name__),
                "given_data": f"El usuario eliminó al empleado con id {ide}."
            }
            Traceability.objects.create(**data_trace)

            return JsonResponse({"message": f"Se eliminó con éxito al empleado con id {ide}"}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)