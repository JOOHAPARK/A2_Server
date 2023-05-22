from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db import connection
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import requests
import json
from django.http import JsonResponse
from .serializers import LikeSerializer



@method_decorator(ensure_csrf_cookie, name='dispatch')
class InfoAPI(APIView):
    def get(self, request):
        # Flask 서버 URL
        flask_server_url = 'http://127.0.0.1:5000/db_check'  

        # GET 요청으로 Flask 서버에 전송
        print(requests.get(flask_server_url))
        response = requests.get(flask_server_url, params=request.query_params)
        if response.status_code == 200:
            data = response.json()
            user = request.user
            for item in data['body']:
                like_id = item['id']  # 예시에서는 Info 모델의 ID로 가정
                info = likes.objects.get(id=like_id)
                item['liked'] = info.liked_users.filter(id=user.id).exists()
                item['like_count'] = info.like_count
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        like_id = request.GET.get('like_id')  # 좋아요를 취소할 Like 객체의 ID
        user = request.user

        try:
            like = likes.objects.get(id=like_id)  # Like 모델에서 해당 ID의 객체 가져오기
        except likes.DoesNotExist:
            return Response({'error': 'Like object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if like.liked_users.filter(id=user.id).exists():  # 사용자가 좋아요를 누른 경우에만 처리
            like.liked_users.remove(user)  # 좋아요 취소
            like.like_count -= 1  # 좋아요 수 감소
            like.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def post(self, request):
    #     # 좋아요 처리 로직
    #     data = request.data  # POST 요청으로 전달된 데이터
    #     like_id = data.get('like_id')

    #     try:
    #         info = likes.objects.get(id=like_id)
    #     except likes.DoesNotExist:
    #         return Response({'error': 'Invalid like_id'}, status=status.HTTP_400_BAD_REQUEST)

    #     user = request.user
    #     liked = info.toggle_like(user)

    #     return Response({'liked': liked}, status=status.HTTP_200_OK)




# class MyView(APIView):
#     def post(self, request):
#         # 사용자 입력 받기
#         facilities_type = request.data.get('facilities_type', " ")
#         lat = request.data.get('lat', '')
#         lon = request.data.get('lon', '')
#         radius = request.data.get('radius', '')

#         # Flask 서버 URL
#         flask_server_url = 'http://127.0.0.1:5000/db_check'

#         # GET 요청으로 Flask 서버에 데이터 전송
#         params = {
#             'facilities_type':  facilities_type,
#             'lat': lat,
#             'lon': lon,
#             'radius': radius
#         }
#         json_data = json.dumps(params)
#         print(json_data)
#         response = requests.get(flask_server_url, params = json_data)
#         print(response)
#         if response.status_code == 200:
#             data = response.json()
#             return Response(data['body'], status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)