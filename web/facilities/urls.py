from django.urls import include, path
from .views import *

app_name = "facilities"

urlpatterns = [
    path('info/', InfoAPI.as_view()),
]