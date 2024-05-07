from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from data import helpers


class post_verif_code(APIView):
    permission_classes = []

    def post(self, request):
        input_params = request.data
        try:
            if not "@unal.edu.co" in input_params["email"]:
                raise ValueError("El correo no es dominio @unal.edu.co")

            helpers.sent_email_verif_code(input_params["email"], input_params["id"])

            return JsonResponse({'mensaje': f'Se envió el código de verificación al correo {input_params["email"]}'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)