from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# 반경 radius * 0.001
  

# 입력받은 반경 병원 정보 조회
class hospitalAPI(APIView):
    def post(self,request):
         hospital_serializer = UserInputSerializer(data = request.data)
         if hospital_serializer.is_valid():
            result = hospital_serializer.data['x']
            result2 = hospital_serializer.data['y']
            radius = hospital_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
        
            filter_kwargs['x__gte'] = result - radius * 0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001


            try:
                position = Hospital.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Hospital.objects.all()
            
            for hospital_data in position:
                hospital_data.choice = True

            serializer = HospitalSerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 병원 값들만 보여주기
# class getHospitalAPI(APIView):
#     def get(self, request):
#         info = Hospital.objects.filter(choice=True)
#         serializer = HospitalSerializer(info, many=True)
#         return Response(serializer.data)



# 입력받은 반경 체육시설 정보 조회
class gymAPI(APIView):
    def post(self,request):
         gym_serializer = UserInputSerializer(data = request.data)
         if gym_serializer.is_valid():
            gym_serializer.save()
            result = gym_serializer.data['x']
            result2 = gym_serializer.data['y']
            radius = gym_serializer.data['radius']
            

            
            filter_kwargs = {}
        

            filter_kwargs['x__gte'] = result - radius*0.001
            print(result - radius*0.001) 
            filter_kwargs['x__lte'] = result + radius*0.001
            print(result + radius*0.001) 
            filter_kwargs['y__gte'] = result2 - radius*0.001
            print(result2 - radius*0.001) 
            filter_kwargs['y__lte'] = result2 + radius*0.001
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

# 카테고리 선택한 체육시설 값들만 보여주기
# class getGymAPI(APIView):
#     def get(self, request):
#         info = Gym.objects.filter(choice=True)
#         serializer = GymSerializer(info, many=True)
#         return Response(serializer.data)

# 입력받은 반경 미용실 정보 조회
class hairAPI(APIView):
    def post(self,request):
         hair_serializer = UserInputSerializer(data = request.data)
         if hair_serializer.is_valid():
            result = hair_serializer.data['x']
            result2 = hair_serializer.data['y']
            radius = hair_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Hair.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Hair.objects.all()
            
            for hair_data in position:
                hair_data.choice = True
            serializer = HairSerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 미용실 값들만 보여주기
# class getHairAPI(APIView):
#     def get(self, request):
#         info = Hair.objects.filter(choice=True)
#         serializer = HairSerializer(info, many=True)
#         return Response(serializer.data)
    
# 입력받은 반경 런드리 정보 조회
class laundryAPI(APIView):
    def post(self,request):
         laundry_serializer = UserInputSerializer(data = request.data)
         if laundry_serializer.is_valid():
            result = laundry_serializer.data['x']
            result2 = laundry_serializer.data['y']
            radius = laundry_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Laundry.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Laundry.objects.all()
            
            for laundry_data in position:
                laundry_data.choice = True
            serializer = LaundrySerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 런드리 값들만 보여주기
# class getLaundryAPI(APIView):
#     def get(self, request):
#         info = Laundry.objects.filter(choice=True)
#         serializer = LaundrySerializer(info, many=True)
#         return Response(serializer.data)


# 입력받은 반경 약국 정보 조회
class pharmacyAPI(APIView):
    def post(self,request):
        pharmacy_serializer = UserInputSerializer(data = request.data)
        if pharmacy_serializer.is_valid():
            result = pharmacy_serializer.data['x']
            result2 = pharmacy_serializer.data['y']
            radius = pharmacy_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Pharmacy.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Pharmacy.objects.all()
            
            for pharmacy_data in position:
                pharmacy_data.choice = True
            serializer = PharmacySerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 약국 값들만 보여주기
# class getPharmacyAPI(APIView):
#     def get(self, request):
#         info = Pharmacy.objects.filter(choice=True)
#         serializer = PharmacySerializer(info, many=True)
#         return Response(serializer.data)
    

# 입력받은 반경 마트 정보 조회
class martAPI(APIView):
    def post(self,request):
         mart_serializer = UserInputSerializer(data = request.data)
         if mart_serializer.is_valid():
            result = mart_serializer.data['x']
            result2 = mart_serializer.data['y']
            radius = mart_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Mart.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Mart.objects.all()
            
            for mart_data in position:
                mart_data.choice = True
            serializer = MartSerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 마트 값들만 보여주기
# class getMartAPI(APIView):
#     def get(self, request):
#         info = Mart.objects.filter(choice=True)
#         serializer = MartSerializer(info, many=True)
#         return Response(serializer.data)
    

# 입력받은 반경 카페 정보 조회
class cafeAPI(APIView):
    def post(self,request):
         cafe_serializer = UserInputSerializer(data = request.data)
         if cafe_serializer.is_valid():
            result = cafe_serializer.data['x']
            result2 = cafe_serializer.data['y']
            radius = cafe_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Cafe.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Cafe.objects.all()
            
            for cafe_data in position:
                cafe_data.choice = True
            serializer = CafeSerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 카페 값들만 보여주기
# class getCafeAPI(APIView):
#     def get(self, request):
#         info = Cafe.objects.filter(choice=True)
#         serializer = CafeSerializer(info, many=True)
#         return Response(serializer.data)


# 입력받은 반경 편의점 정보 조회
class convenienceAPI(APIView):
    def post(self,request):
         convenience_serializer = UserInputSerializer(data = request.data)
         if convenience_serializer.is_valid():
            result = convenience_serializer.data['x']
            result2 = convenience_serializer.data['y']
            radius = convenience_serializer.data['radius']
            
            filter_kwargs = {}
            filter_kwargs = {}
           			
            filter_kwargs['x__gte'] = result - radius*0.001 
            filter_kwargs['x__lte'] = result + radius*0.001
            filter_kwargs['y__gte'] = result2 - radius*0.001
            filter_kwargs['y__lte'] = result2 + radius*0.001
            try:
                position = Convenience.objects.filter(**filter_kwargs)
                
            except ValueError:
                position = Convenience.objects.all()
            
            for convenience_data in position:
                convenience_data.choice = True
            serializer = ConvenienceSerializer(position, many=True)
            return Response(serializer.data)

# 카테고리 선택한 편의점 값들만 보여주기
# class getConvenienceAPI(APIView):
#     def get(self, request):
#         info = Convenience.objects.filter(choice=True)
#         serializer = ConvenienceSerializer(info, many=True)
#         return Response(serializer.data)
    


    
# def share(request, x, y):
#  post = Post.objects.all()
# For (위도,경도) in post:
# 	if lagti == x and if 경도 == y:
# serializer = GetSerializer(post, many = True)
# Return Response (serializer.data)

