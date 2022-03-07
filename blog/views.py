from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import FileResponse
from django.shortcuts import render
from django.utils.encoding import escape_uri_path
from AuthManage import models
from .models import article, ArticleType, ArticleComment


def index(request):
    username = request.user.username
    if username:
        Obj = models.User.objects.filter(username=username).first()
        NickName = Obj.userinftable.NickName
    return render(request, 'index.html', context=locals())


def RegisterRobot(request):
    Demoname = '信息登记机器人'
    return render(request, 'projectshow/RegisterRobot.html', context=locals())


def WebDevelop(request):
    Demoname = 'Web开发'
    return render(request, 'projectshow/WebDevelop.html', context=locals())


def GobangDevelop(request):
    Demoname = '深度学习博弈'
    return render(request, 'projectshow/GobangDevelop.html', context=locals())


def downloadrobot(request, RobotId):
    file = None
    if RobotId == 0:
        file = open(r'C:\inetpub\wwwroot\tigerhowl\static\doc\信息登记机器人0.zip', 'rb')
    elif RobotId == 1:
        file = open(r'C:\inetpub\wwwroot\tigerhowl\static\doc\信息登记机器人1.zip', 'rb')
    elif RobotId == 2:
        file = open(r'C:\inetpub\wwwroot\tigerhowl\static\doc\定时播报机器人.zip', 'rb')
    file_name = '信息登记机器人.zip'
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response


def downloadweb(request):
    file = open(r'C:\inetpub\wwwroot\tigerhowl\static\doc\数学建模协会官网.zip', 'rb')
    file_name = '数学建模协会官网.zip'
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response


def TitleList(request):
    ArticleTypeId = int(request.GET.get('ArticleTypeId'))
    page_index = int(request.GET.get('page_index'))
    if ArticleTypeId == 0:
        TitleObj = article.objects.all()
    else:
        TitleObj = article.objects.all().filter(articletype=ArticleTypeId)
    paginator = Paginator(TitleObj, 4)
    page = paginator.page(page_index)
    ArticleTypeObj = ArticleType.objects.all()
    username = request.user.username
    if username:
        Obj = models.User.objects.filter(username=username).first()
        NickName = Obj.userinftable.NickName
    return render(request, 'Blog/TitleList.html', context=locals())


def ArticleRequset(request, ArticleId):
    if request.method == 'GET':
        TitleObj = article.objects.get(id=ArticleId)
        ArticleTypeObj = ArticleType.objects.all()
        TitleObj.LookTime = TitleObj.LookTime + 1
        TitleObj.save()  # 增加浏览量
        username = request.user.username
        if username:
            Obj = models.User.objects.filter(username=username).first()
            NickName = Obj.userinftable.NickName
        FirstCommentObj = TitleObj.articlecomment_set.all()
        return render(request, 'Blog/article.html', context=locals())
    else:
        TitleObj = article.objects.get(id=ArticleId)
        ArticleTypeObj = ArticleType.objects.all()
        Obj = models.User.objects.get(username=request.user.username)
        NickName = Obj.userinftable.NickName
        TitleObj.articlecomment_set.create(context=request.POST['FirstComment'], CommentUser=NickName)
        FirstCommentObj = TitleObj.articlecomment_set.all()
        TitleObj.CommentTime = ArticleComment.objects.filter(CommentedArticle_id=ArticleId).count()
        TitleObj.save()
        return render(request, 'Blog/article.html', context=locals())


def SecondComment(request, ArticleId, CommentId):
    TitleObj = article.objects.get(id=ArticleId)
    CommentObj = TitleObj.articlecomment_set.get(id=CommentId)
    Obj = models.User.objects.get(username=request.user.username)
    NickName = Obj.userinftable.NickName
    SecondCommentObj = CommentObj.secnodcomment_set.create(CommentUser=NickName, context=request.POST['SecondComment'])
    SecondCommentObj.save()
    FirstCommentObj = TitleObj.articlecomment_set.all()
    return render(request, 'Blog/article.html', context=locals())


def BookSnail(request):
    Demoname = '书蜗行动'
    return render(request, 'projectshow/BookSnail.html', context=locals())


def downloadbooksnail(request):
    file = open(r'C:\inetpub\wwwroot\tigerhowl\static\doc\书蜗抢座.zip', 'rb')
    file_name = '书蜗抢座.zip'
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response

