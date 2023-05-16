from django.db import models

# Create your models here.


class Notice(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True)
    contact=models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
