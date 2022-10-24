from django.urls import path
from backendapp.views import *

urlpatterns=[
    path('', TodoView.as_view(), name= 'initial'),
    path("create_user", UserInfo.as_view(), name="user workarounds"),
    path("get_user_info", UserInfo.as_view(), name="get user info"),
    path("log_in", UserInfo.as_view(), name="log in"),
    path("search_todo", TodoView.as_view(), name="search todo")
]