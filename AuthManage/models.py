from django.db import models
from django.contrib.auth.models import User


class UserInfTable(models.Model):
    UserInf=models.OneToOneField(User,on_delete=models.CASCADE)
    NickName=models.CharField(max_length=15,unique=True)
    RealName=models.CharField(max_length=10,blank=True)
    class Meta:
        db_table='UserInf'

class muteuser(models.Model):
    qqnumber=models.CharField(max_length=20,unique=True)
    qqmessage1=models.TextField(null=True)
    qqmessage2=models.TextField(null=True)
    qqmessage3=models.TextField(null=True)
    qqmessagetimes=models.IntegerField(default=0)
    lastmessagedate=models.DateTimeField()
    class Meta:
        db_table='muteuser'