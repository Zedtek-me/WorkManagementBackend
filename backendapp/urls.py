from django.urls import path
from backendapp.views import *

urlpatterns=[
    path('', TodoView.as_view(), name= 'initial'),
    path("create_user", UserInfo.as_view(), name="user workarounds"),
    path("get_user_info/<int:pk>", UserInfo.as_view(), name="get user info"),
    path("log_in", UserInfo.as_view(), name="log in")
]