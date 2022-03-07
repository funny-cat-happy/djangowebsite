from django.urls import path, include
from transaction import views

urlpatterns = [
    path('GoodsList/', views.GoodsList, name='GoodsList'),
]
