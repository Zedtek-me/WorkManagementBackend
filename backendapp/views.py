from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class TestView(APIView):
    '''
    To test restframework implementations for now.
    '''
    def get(self, request):
        return Response({"welcome": "this is just a test view for now."}, status.HTTP_200_OK)

    def post(self, request):
        data= request.data
        print(data)
        return Response({"sent_data": data}, status.HTTP_200_OK)
