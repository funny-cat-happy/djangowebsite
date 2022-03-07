"""tigerhowl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from blog import views
from tigerhowl.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('AuthManage/', include(('AuthManage.urls', 'AuthManage'), namespace='AuthManage')),
    path('travel/', include(('travel.urls', 'travel'), namespace='travel')),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('transaction/', include(('transaction.urls', 'transaction'), namespace='transaction')),
    path('favicon.ico/', RedirectView.as_view(url=STATIC_URL + 'favicon.ico'))
]

# from django.conf import settings
# from django.conf.urls.static import static
# STATIC_URL = '/static/'
# urlpatterns += static(settings,STATIC_URL,document_root=settings.STATIC_ROOT)
