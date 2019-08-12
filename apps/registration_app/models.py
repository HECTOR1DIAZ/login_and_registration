from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) == 0:
            errors["firstname"] = "Please enter your first name"
            
        if len(postData['lastname']) == 0:
            errors["lastname"] = "Show description should be at least 5 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 25,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    objects = ShowManager()


