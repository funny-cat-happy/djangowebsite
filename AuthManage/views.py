import os
import random
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse, HttpResponseRedirect
from six import BytesIO
from tigerhowl import settings
from .form import UserRegisterForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .models import UserInfTable


def Login(request):
    if request.method=='POST':
        username=request.POST['UserAccount']
        password=request.POST['UserPassword']
        UserObj=authenticate(request,username=username,password=password)
        if UserObj:
            login(request,UserObj)
            return HttpResponseRedirect('/')
        else:
            error='登录失败'
            return render(request,'AuthManage/LoginUI.html',context=locals())
    else:
        return render(request, 'AuthManage/LoginUI.html')


def Register(request):
    if request.method=='POST':
        UserInputCode=request.POST.get('VerCode')
        ProduceCode=request.session.get('Vercode')
        if UserInputCode==ProduceCode:
            RegisterForm=UserRegisterForm(request.POST)
            if RegisterForm.is_valid():
                RegisterForm.save()
                UserObj=authenticate(request,username=RegisterForm.cleaned_data['username'],password=RegisterForm.cleaned_data['password1'])
                login(request,UserObj)
                UserInfTable(UserInf=UserObj,NickName=RegisterForm.cleaned_data['NickName'],RealName=RegisterForm.cleaned_data['RealName']).save()
                return HttpResponseRedirect('/')
            else:
                return render(request, 'AuthManage/RegisterUl.html',context=locals())
        else:
            VercodeError='验证码输入错误'
            return render(request,'AuthManage/RegisterUl.html',context=locals())
    else:
        # RegisterForm = UserRegisterForm
        return render(request,'AuthManage/RegisterUl.html')


def Logout(request):
    logout(request)
    return  HttpResponseRedirect('/')


def GetCode(request,key):
    height=80
    width=30
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ImageFile = Image.new(mode='RGB', size=(height, width), color=color1)
    ImagePencil = ImageDraw.Draw(ImageFile, mode='RGB')
    ImageFonts = ImageFont.truetype(font=os.path.join(settings.STATICFILES_DIRS[0],'fonts/wqy.ttf'), size=height//4)
    Vercode = ['陕', '西', '理', '工', '大', '学']
    random.shuffle(Vercode)
    text = ''.join(Vercode[0:4])
    for i in range(0, 4):  # 绘制文本
        color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ImagePencil.text(xy=((height//4)* i, 0), text=text[i], font=ImageFonts, fill=color3)
    for i in range(0, height//5):  # 绘制干扰点
        for j in range(0, width//5):
            color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ImagePencil.point(xy=(i * 5, j * 5), fill=color2)
    request.session['Vercode']=text
    fp = BytesIO()
    ImageFile.save(fp=fp, format='png')
    return HttpResponse(fp.getvalue(),content_type='image/png')


def PrivacyError(request):
    return render(request,'ErrorPage/SeePrivacy.html')