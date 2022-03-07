from django.urls import path
from AuthManage import views

urlpatterns = [
    path('Login/',views.Login,name='Login'),
    path('Logout/',views.Logout,name='Logout'),
    path('Register/',views.Register,name='Register'),
    path('GetCode/<int:key>',views.GetCode,name='GetCode'),
    path('PrivacyError/',views.PrivacyError,name='PrivacyError')

]
