from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('', TodoView.as_view(), name= 'initial')
]