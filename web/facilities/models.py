from django.db import models

class UserInput(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    radius = models.IntegerField(null=True)

class Bus(models.Model):
    CityName = models.CharField(max_length=50)
    StationName = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Hospital(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Gym(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Hair(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)



class Laundry(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Pharmacy(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Mart(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)


class Cafe(models.Model):
    bplcNm = models.CharField(max_length=50)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choice = models.BooleanField(default=False)



class Convenience(models.Model):
    bplcNm = models.CharField(max_length=50)
    siteWhlAddr = models.CharField(max_length=200)
    rdnWhlAddr = models.CharField(max_length=200)
    uptaeNm = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    choose = models.BooleanField(default=False)