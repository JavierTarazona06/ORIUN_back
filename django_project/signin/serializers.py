import pytz

from datetime import datetime, timedelta
from traceability.models import Traceability
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from data import helpers

#HOUR_COL = datetime.now(pytz.timezone('Etc/GMT-5'))
#HOUR_COL = datetime.now(pytz.timezone('America/Bogota'))
#HOUR_COL = datetime.now(pytz.timezone('Etc/GMT-0')) - timedelta(hours=5)
HOUR_COL = helpers.get_col_time()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        token = super().validate(attrs)

        data_trace = {
            "user": self.user,
            "time": str(HOUR_COL),
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
