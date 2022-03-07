from django.db import models

class GoodsType(models.Model):
    type = models.CharField(max_length=15)
    def __str__(self):
        return self.type


class GoodsInformation(models.Model):
    GoodsOwner=models.CharField(max_length=10)
    GoodsName=models.CharField(max_length=30)
    GoodsKind=models.ForeignKey(GoodsType,on_delete=models.DO_NOTHING)
    CreateTime = models.DateTimeField(auto_now_add=True)
    ContactMethod=models.CharField(max_length=20)
    BuyPrice=models.IntegerField()
    SellPrice=models.IntegerField()
    FirstImageName=models.CharField(max_length=10,default='无')
    SecondImageName=models.CharField(max_length=10,default='无')
    ThirdImageName=models.CharField(max_length=10,default='无')
    def __str__(self):
        return self.GoodsName