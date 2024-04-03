from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        token = super().validate(attrs)
        if hasattr(self.user, 'student'):
            token['type_user'] = 'student'
        elif hasattr(self.user, 'employee'):
            token['type_user'] = 'employee'
        else:
            token['type_user'] = 'unknown'
        return token
