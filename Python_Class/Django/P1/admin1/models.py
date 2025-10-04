from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True,null=True)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery/',null=True)
    def __str__(self):
        return self.name