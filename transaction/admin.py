from django.contrib import admin
from .models import GoodsType,GoodsInformation


@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

@admin.register(GoodsInformation)
class articleAdmin(admin.ModelAdmin):
    list_display = ('GoodsOwner','GoodsName','GoodsKind','ContactMethod','BuyPrice','SellPrice','FirstImageName','SecondImageName','ThirdImageName')



