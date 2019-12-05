from django.db import models

# Create your models here.

class SignupInfo(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    username=models.CharField(unique=True, max_length=100)
    password=models.CharField(max_length=100)
    create_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.username