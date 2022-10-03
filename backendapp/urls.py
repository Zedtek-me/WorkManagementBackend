from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('', TestView.as_view(), name= 'initial')
]