from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
# Create your models here.

class UserManager(BaseUserManager):
    '''
    custom user manager. Has two methods: create_user and create_superuser
    '''
    def create_user(self, **user_info:dict)->AbstractUser:
        if not user_info.get("email"):
            raise ValidationError("You have to include an email address.")
        user= self.model(**user_info)
        user.set_password(user_info.get("password", user_info.get("password1")))
        user.save()
        return user

    def create_superuser(self, **user_info):
        user= self.create_user(**user_info)
        user.is_staff= True
        user.is_superuser=True
        user.is_admin= True
        user.save()
        return user

class User(AbstractUser, PermissionsMixin):
    name=models.CharField(max_length=200, blank=False, null=False)
    other_name= models.CharField(max_length=200, blank=False, null=False)
    username= models.CharField(max_length=200, blank=False, null=False)
    email= models.EmailField(max_length=200, blank=False, null=False, unique=True)
    phone_num= models.CharField(max_length=200, blank=True, null=True)
    profile_image= models.ImageField(upload_to="userImages", default="default.jpg", null=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)
    password= models.CharField(max_length=5000000, blank=False, null=False)

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= ["name", "other_name", "username", "phone_num"]

    # user manager
    objects= UserManager()
