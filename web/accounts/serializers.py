from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','username']