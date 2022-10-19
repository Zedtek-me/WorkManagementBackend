from rest_framework.serializers import *
from backendapp.todo_models import *
from backendapp.models import User
class TodoSerializer(ModelSerializer):
    '''
    serializes todo activities.
    '''
    owner= StringRelatedField()
    class Meta:
        model= Todo
        fields= "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        exclude=["password"]