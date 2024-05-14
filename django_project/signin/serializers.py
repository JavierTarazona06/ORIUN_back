from datetime import datetime
from traceability.models import Traceability
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        token = super().validate(attrs)

        data_trace = {
            "user": self.user,
            "time": datetime.now(),
            "method": 'GET',
            "view": 'LogIn',
            "given_data": f'El usuario ha ingresado'
        }
        Traceability.objects.create(**data_trace)

        if hasattr(self.user, 'student'):
            token['type_user'] = 'student'
        elif hasattr(self.user, 'employee'):
            token['type_user'] = 'employee'
        else:
            token['type_user'] = 'unknown'
        return token
