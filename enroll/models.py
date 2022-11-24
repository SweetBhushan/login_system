from tkinter import Widget
from django.db import models

# Create your models here.
class studentRegistration(models.Model):
    username= models.CharField(max_length=70)
    first_name=models.CharField(max_length=70)
    Last_name= models.CharField(max_length=70)
    email= models.EmailField(max_length=70)
    password=models.CharField(max_length=70)