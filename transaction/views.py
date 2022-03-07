from django.core.paginator import Paginator
from django.shortcuts import render
from AuthManage import models
from .models import GoodsType,GoodsInformation

def GoodsList(request):
    GoodsTypeId = int(request.GET.get('GoodsTypeId'))
    page_index = int(request.GET.get('page_index'))
    if GoodsTypeId == 0:
        GoodsObj = GoodsInformation.objects.all()
    else:
        GoodsObj = GoodsInformation.objects.all().filter(GoodsKind=GoodsTypeId)
    paginator = Paginator(GoodsObj, 4)
    page = paginator.page(page_index)
    GoodsTypeObj = GoodsType.objects.all()
    username = request.user.username
    if username:
        Obj = models.User.objects.filter(username=username).first()
        NickName = Obj.userinftable.NickName
    return render(request, 'GoodsList/MainList.html', context=locals())