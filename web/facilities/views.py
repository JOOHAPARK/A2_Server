from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
# from django.contrib.gis.geos import GEOSGeometry
# import json



  

# 입력받은 반경 병원 정보 조회
class hospitalAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         hospital_serializer = UserInputSerializer(data = data_tmp )
         
         if hospital_serializer.is_valid():
            result = hospital_serializer.data['st_x']
            result2 = hospital_serializer.data['st_y']
            radius = hospital_serializer.data['radius']
            
            filter_kwargs = {}
        
            filter_kwargs['st_x__gte'] = result - radius * 0.000001 
            filter_kwargs['st_x__lte'] = result + radius * 0.000001
            filter_kwargs['st_y__gte'] = result2 - radius * 0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius * 0.0000015


            try:
                position = Hospital.objects.filter(**filter_kwargs)
                for hospital_data in position:
                    hospital_data.choice = True
                
            except ValueError:
                position = Hospital.objects.all()
            
        

            

            serializer = HospitalSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





# 입력받은 반경 체육시설 정보 조회
class gymAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         gym_serializer = UserInputSerializer(data = data_tmp)
         if gym_serializer.is_valid():
            gym_serializer.save()
            result = gym_serializer.data['st_x']
            result2 = gym_serializer.data['st_y']
            radius = gym_serializer.data['radius']
            
            # geom = GEOSGeometry(Gym.coordinates)
            # json_data = json.loads(geom.json)
            # result = json_data[0]
            # result2 = json_data[1]

            
            filter_kwargs = {}
        

            filter_kwargs['st_x__gte'] = result - radius*0.000001
            print(result - radius*0.001) 
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            print(result + radius*0.001) 
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            print(result2 - radius*0.001) 
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            print(result2 + radius*0.001) 
            
            try:
                position = Gym.objects.filter(**filter_kwargs)
                for gym_data in position:
                    gym_data.choice = True

                
                
            
            except ValueError:
                position = Gym.objects.all()
            

            serializer = GymSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 입력받은 반경 미용실 정보 조회
class hairAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         hair_serializer = UserInputSerializer(data = data_tmp)
         if hair_serializer.is_valid():
            result = hair_serializer.data['st_x']
            result2 = hair_serializer.data['st_y']
            radius = hair_serializer.data['radius']
            
            filter_kwargs = {}

           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001 
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Hair.objects.filter(**filter_kwargs)
                for hair_data in position:
                    hair_data.choice = True
                
            except ValueError:
                position = Hair.objects.all()
            
           
            
            serializer = HairSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




    
# 입력받은 반경 런드리 정보 조회
class laundryAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         laundry_serializer = UserInputSerializer(data = data_tmp)
         if laundry_serializer.is_valid():
            result = laundry_serializer.data['st_x']
            result2 = laundry_serializer.data['st_y']
            radius = laundry_serializer.data['radius']
            
            filter_kwargs = {}
    
           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Laundry.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Laundry.objects.all()
            
            for laundry_data in position:
                laundry_data.choice = True


            serializer = LaundrySerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




# 입력받은 반경 약국 정보 조회
class pharmacyAPI(APIView):
    def post(self,request):
        data_tmp = request.data['user_json']
        pharmacy_serializer = UserInputSerializer(data = data_tmp)
        if pharmacy_serializer.is_valid():
            result = pharmacy_serializer.data['st_x']
            result2 = pharmacy_serializer.data['st_y']
            radius = pharmacy_serializer.data['radius']
            
            filter_kwargs = {}

           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Pharmacy.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Pharmacy.objects.all()
            
            for pharmacy_data in position:
                pharmacy_data.choice = True

            serializer = PharmacySerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    

# 입력받은 반경 마트 정보 조회
class martAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         mart_serializer = UserInputSerializer(data = data_tmp)
         if mart_serializer.is_valid():
            result = mart_serializer.data['st_x']
            result2 = mart_serializer.data['st_y']
            radius = mart_serializer.data['radius']
            
            filter_kwargs = {}

           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001 
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Mart.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Mart.objects.all()
            
            for mart_data in position:
                mart_data.choice = True

            serializer = MartSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    

# 입력받은 반경 카페 정보 조회
class cafeAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         cafe_serializer = UserInputSerializer(data = data_tmp)
         if cafe_serializer.is_valid():
            result = cafe_serializer.data['st_x']
            result2 = cafe_serializer.data['st_y']
            radius = cafe_serializer.data['radius']
            
            filter_kwargs = {}

           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Cafe.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Cafe.objects.all()
            
            for cafe_data in position:
                cafe_data.choice = True

            serializer = CafeSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# 카테고리 선택한 카페 값들만 보여주기
# class getCafeAPI(APIView):
#     def get(self, request):
#         info = Cafe.objects.filter(choice=True)
#         serializer = CafeSerializer(info, many=True)
#         return Response(serializer.data)


# 입력받은 반경 편의점 정보 조회
class convenienceAPI(APIView):
    def post(self,request):
         data_tmp = request.data['user_json']
         convenience_serializer = UserInputSerializer(data = data_tmp)
         if convenience_serializer.is_valid():
            result = convenience_serializer.data['st_x']
            result2 = convenience_serializer.data['st_y']
            radius = convenience_serializer.data['radius']
            
            filter_kwargs = {}

           			
            filter_kwargs['st_x__gte'] = result - radius*0.000001
            filter_kwargs['st_x__lte'] = result + radius*0.000001
            filter_kwargs['st_y__gte'] = result2 - radius*0.0000015
            filter_kwargs['st_y__lte'] = result2 + radius*0.0000015
            try:
                position = Convenience.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Convenience.objects.all()
            
            for convenience_data in position:
                convenience_data.choice = True
            serializer = ConvenienceSerializer(position, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    


    
# def share(request, x, y):
#  post = Post.objects.all()
# For (위도,경도) in post:
# 	if lagti == x and if 경도 == y:
# serializer = GetSerializer(post, many = True)
# Return Response (serializer.data)

