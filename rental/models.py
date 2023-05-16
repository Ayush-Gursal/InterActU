from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    
    title=models.CharField(max_length=255)
    price=models.IntegerField(null=True)
    location=models.CharField(max_length=200,null=True)
    ownername=models.CharField(max_length=200,null=True)
    contact=models.IntegerField(null=True)
    id=models.IntegerField(primary_key=True)
    image=models.ImageField(blank=True,null=True)
    ownername=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/') 

    def __str__(self):
        return self.post.title
    









