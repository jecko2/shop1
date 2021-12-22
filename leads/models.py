from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.email
    

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_addr = models.EmailField(unique=True, max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email_addr
    