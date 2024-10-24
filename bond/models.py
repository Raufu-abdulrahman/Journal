from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    quote = models.TextField()

    def __str__(self):
        return self.name
    
class Journal(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username