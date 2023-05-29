from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    typ = models.CharField(max_length=20)
    slug = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.typ

class Membershib(models.Model):
    account = models.ForeignKey(User,related_name="membershib",on_delete=models.CASCADE)
    m_type = models.ForeignKey(Category,related_name="membershib",on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.m_type.typ