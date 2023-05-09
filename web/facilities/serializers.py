from rest_framework import serializers
from .models import *

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['st_x','st_y','radius']


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']

class ConvenienceSerializer(serializers.ModelSerializer):
    class Meat:
        model = Convenience
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']

class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']

        

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']


class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']


class MartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mart
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'st_x','st_y','choice']




