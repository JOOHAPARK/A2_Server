from rest_framework import serializers
from .models import *

class UserInput(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    radius = models.FloatField()

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = [ 'x','y','radius']


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

class MartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mart
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['bplcnm', 'uptaenm', 'x','y','choice']

class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'x','y','choice']

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

class LaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laundry
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

class ConvenienceSerializer(serializers.ModelSerializer):
    class Meat:
        model = Convenience
        fields = ['bplcnm', 'sitewhladdr', 'rdnwhladdr', 'uptaenm', 'x','y','choice']

