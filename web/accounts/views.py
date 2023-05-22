from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from .serializers import LoginSerializer, SignupSerializer
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')
class loginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = auth.authenticate(
                request=request,
                email=serializer.data['email'],
                password=serializer.data['password']
            )
            if user is not None:
                auth.login(request, user)
                response = JsonResponse({'message': '로그인 되었습니다.'})
                response.set_cookie('sessionid', request.session.session_key)
                return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class signup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save(password = make_password(serializer.validated_data['password']))
            return Response({"user" : serializer.data['username'], "email":serializer.data['email']},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class logout(APIView):
    def get(self, request):
        auth.logout(request)
        return Response({'message':'로그아웃 완료'},status=status.HTTP_200_OK)