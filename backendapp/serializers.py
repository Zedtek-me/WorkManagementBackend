from rest_framework.serializers import ModelSerializer
from .todo_models import *

class TodoSerializer(ModelSerializer):
    '''
    serializes todo activities.
    '''
    class Meta:
        model= Todo
        fields= "__all__"