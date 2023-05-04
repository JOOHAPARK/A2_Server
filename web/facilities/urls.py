from django.urls import include, path
from .views import *

app_name = "facilities"

urlpatterns = [
    path('bus/', busAPI.as_view()),
    path('hospital/', hospitalAPI.as_view()),
    path('gym/', gymAPI.as_view()),
    path('hair/', hairAPI.as_view()),
    path('laundry/', laundryAPI.as_view()),
    path('pharmacy/', pharmacyAPI.as_view()),
    path('mart/', martAPI.as_view()),
    path('cafe/', cafeAPI.as_view()),
    path('convenience/', convenienceAPI.as_view()),
    path('getbus/', getbusAPI.as_view()),
    path('gethosp/', getHospitalAPI.as_view()),
    path('getgym/', getGymAPI.as_view()),
    path('gethair/', getHairAPI.as_view()),
    path('getlaun/', getLaundryAPI.as_view()),
    path('getpharm/', getPharmacyAPI.as_view()),
    path('getmart/', getMartAPI.as_view()),
    path('getcafe/', getCafeAPI.as_view()),
    path('getconv/', getConvenienceAPI.as_view()),


]