from django.db import models
from user.models import SignupInfo
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.

class BlogCategories(models.Model):
    category =  models.CharField(max_length=50)

    def __str__(self):
        return self.category

class BlogCrete(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=100)
    category = models.ManyToManyField(BlogCategories)
    content = models.TextField()
    feature_img = models.ImageField(upload_to='blogs/%Y/%m/%d')
    blog_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
