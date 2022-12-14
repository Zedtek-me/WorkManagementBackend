from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from backendapp.todo_models import *
from backendapp.serializers import *
from django.contrib.auth import login, authenticate
from django.db.models import Q
import json
# Create your views here.


class TodoView(APIView):
    '''
    To test restframework implementations for now.
    '''
    def get(self, request):
        if not request.query_params:
            # to get all todo activities
            todo= Todo.objects.all()
            serialized_todo= TodoSerializer(todo, many=True)
            return Response(serialized_todo.data, status.HTTP_200_OK)
        # otherwise get one activity
        pk= request.query_params.get("pk")
        try:
            todo= Todo.objects.get(pk=int(pk))
        except Todo.DoesNotExist:
            return Response({"not_found" :"this activity does not exist in the database."}, status.HTTP_404_NOT_FOUND)
        serialized_single_todo= TodoSerializer(todo)
        return Response({"todo":serialized_single_todo.data}, status.HTTP_200_OK)

    def post(self, request):
        if not "To-Create-Todo" in request.headers:
            # meant to search for a data at the backend
            data= json.loads(request.body)
            db_data= Todo.objects.filter(Q(item__icontains=data.get("query"))| Q(name__icontains=data.get("query")))
            if db_data:
                serialized_result= TodoSerializer(db_data, many=True)
                return Response(serialized_result.data, status.HTTP_200_OK)
        # create a new todo record
        else:
            data= request.data
            serialized= TodoSerializer(data=data)
            if serialized.is_valid():
                return Response({"todo": serialized.data}, status.HTTP_200_OK)
            return Response({"sent_data": data}, status.HTTP_200_OK)


class UserInfo(APIView):
    '''
    handles all user activities, including authentication, permission and session data
    '''
    def get(self, request):
        '''
        to get a user detail: logged in or not
        '''
        params= request.query_params
        if params:
            '''
            gets a single user if there's a query parameter in the get request.
            '''
            try:
                user= User.objects.get(id=int(params.get("pk")))
            except User.DoesNotExist:
                print("user not exist")
                return Response({"not_a_user": "this user does not exist"}, status.HTTP_404_NOT_FOUND)
            serialized_user= UserSerializer(user)
            return Response({"user": serialized_user.data}, status.HTTP_200_OK)
        # otherwise return the entire users
        users= User.objects.all()
        serialized_users= UserSerializer(users, many=True)
        return Response(serialized_user.data, status.HTTP_200_OK)
    
    def post(self, request):
        '''
        creates a new user 
        '''
        data= request.data
        if not "To_Log_In" in request.headers:
            # for a create request.
            if (data.get("pass1") and data.get("pass2")) and (data.get("pass1") == data.get("pass2")):
                user= UserSerializer(data=data)
                if user.is_valid():
                    user.save()
                    return Response({"user_created": user.data}, status.HTTP_200_OK)
                return Response({"invalid_credentials": user.errors}, status.HTTP_400_BAD_REQUEST)
            return Response({"invalid_pass": "passwords do not match!"}, status.HTTP_400_BAD_REQUEST)
            
        # for a log in request
        data= request.data
        user= authenticate(request, **data)
        if user:
            login(request, user)
            return Response({"logged_in": "user is logged in."}, status.HTTP_200_OK)
        return Response("invalid credentials!", status.HTTP_400_BAD_REQUEST)