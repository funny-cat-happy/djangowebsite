from django.urls import path, include
from travel import views

urlpatterns = [
    path('main/', views.main_travel, name='MainTravel'),
]
