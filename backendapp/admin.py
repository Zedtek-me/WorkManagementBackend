from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .todo_models import Todo
# Register your models here.
class UserCreationForm(forms.ModelForm):
    """
    aids to create user at the admin interface
    """
    password1= forms.CharField(max_length=300, widget=forms.PasswordInput)
    password2= forms.CharField(max_length=300, widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["name", "username", "email", "other_name"]

    def clean_pass(self):
        pass_one= self.cleaned_data.get("password1")
        pass_two= self.cleaned_data.get("password2")

        if (pass_one and pass_two) and (pass_one == pass_two):
            return pass_one
        return forms.ValidationError("Your Passwords didn't match!")

    def save(self, commit=True):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data.get("pass_one"))
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    '''
    updates user at the admin interface.
    '''
    password= ReadOnlyPasswordHashField()

    class Meta:
        model= User
        fields= ["email", "name", "other_name", "username", "is_active", "is_superuser", "is_staff", "is_admin"]

class UserAdmin(CustomUserAdmin):
    forms= UserUpdateForm()
    add_form= UserCreationForm()
    list_display= ["name", "username", "email", "phone_num"]
    list_filter= ["name", "email", "phone_num"]
    fieldsets=[(None, {"fields": ("name", "username", "other_name")}), ("info", {"fields": ("email","phone_num")}),
    ("perms", {"fields": ("is_staff", "is_superuser", "is_active")})]



admin.site.register(User, UserAdmin)
admin.site.register(Todo)