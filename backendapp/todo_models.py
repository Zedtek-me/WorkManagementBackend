from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()



class Todo(models.Model):
    '''
    main class that handles the todo activities of all users
    '''
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    date_created= models.DateTimeField(auto_now_add= True)
    date_modified= models.DateTimeField(auto_now= True)
    start_date= models.DateTimeField(null=False, blank=False, unique=False)
    end_date= models.DateTimeField(null=False, blank=False, unique=False)

    def __str__(self):
        return self.owner.username + " " + "todo."