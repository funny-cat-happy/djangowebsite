from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def room(request):
    username=request.user.username
    return render(request, 'chat/chat.html',context=locals())
