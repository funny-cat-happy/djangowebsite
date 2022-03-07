from django.urls import path, include
from blog import views

urlpatterns = [
    path('TitleList/', views.TitleList, name='TitleList'),
    path('article/<int:ArticleId>', views.ArticleRequset, name='article'),
    path('SecondComment/<int:ArticleId>/<int:CommentId>', views.SecondComment, name='SecondComment'),
    path('RegisterRobot/', views.RegisterRobot, name='RegisterRobot'),
    path('WebDevelop/', views.WebDevelop, name='WebDevelop'),
    path('GobangDevelop/', views.GobangDevelop, name='GobangDevelop'),
    path('downloadrobot/<int:RobotId>', views.downloadrobot, name='downloadrobot'),
    path('downloadbooksnail/', views.downloadbooksnail, name='downloadbooksnail'),
    path('downloadweb/', views.downloadweb, name='downloadweb'),
    path('BookSnail/', views.BookSnail, name='BookSnail')
]
