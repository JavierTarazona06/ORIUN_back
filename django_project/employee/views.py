from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, EmployeeGetSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from datetime import datetime
from .models import Employee
from django.http import JsonResponse
from rest_framework import status, permissions
from .permissions import IsEmployee


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
            Employee.objects.get(pk=pk)
            my_employee_qset = Employee.objects.filter(pk=pk)
            my_employee_sr = EmployeeGetSerializer(my_employee_qset, many=True).data[0]

            return JsonResponse(my_employee_sr, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
