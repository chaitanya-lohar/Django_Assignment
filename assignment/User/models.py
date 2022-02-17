from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    username=CharField(max_length=50)
    password=CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

    def __str__(self):
        return self.user
