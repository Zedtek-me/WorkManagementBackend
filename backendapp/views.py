from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .todo_models import *
from .serializers import *
# Create your views here.


class TodoView(APIView):
    '''
    To test restframework implementations for now.
    '''
    def get(self, request):
        if not request.query_params:
            todo= Todo.objects.all()
            serialized_todo= TodoSerializer(todo, many=True)
            return Response({"data": serialized_todo.data}, status.HTTP_200_OK)
        pk= request.query_params.get("pk")
        try:
            todo= Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"not_foun" :"this activity does not exist in the database."}, status.HTTP_404_NOT_FOUND)
        serialized_single_todo= TodoSerializer(todo)
        return Response({"todo":serialized_single_todo}, status.HTTP_200_OK)

    def post(self, request):
        data= request.data
        print(data)
        return Response({"sent_data": data}, status.HTTP_200_OK)
