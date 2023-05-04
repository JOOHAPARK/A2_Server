from rest_framework import serializers
from .models import *


# bus, hospital, mart, cafe, hair, laundry, gym, pharmacy, convenience

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['id', 'x','y','position_range']


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'CityName', 'StationName','lat','lon','choice']
    

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

class MartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mart
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id','bplcNm', 'uptaeNm', 'lat','lon','choice']

class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = ['bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'lat','lon','choice']

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

class ConvenienceSerializer(serializers.ModelSerializer):
    class Meat:
        model = Convenience
        fields = ['id','bplcNm', 'siteWhlAddr', 'rdnWhlAddr', 'uptaeNm', 'lat','lon','choice']

