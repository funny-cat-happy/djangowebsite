from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class ArticleType(models.Model):
    type=models.CharField(max_length=15)
    def __str__(self):
        return self.type

class article(models.Model):
    title=models.CharField(max_length=30,unique=True)
    articletype=models.ForeignKey(ArticleType,on_delete=models.DO_NOTHING)
    context=RichTextField(config_name='my_config')
    auth=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    CreateTime=models.DateTimeField(auto_now_add=True)
    ChangeTime=models.DateTimeField(auto_now=True)
    LookTime=models.IntegerField(default=0)
    CommentTime=models.IntegerField(default=0)
    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    CommentedArticle=models.ForeignKey(article,on_delete=models.CASCADE)
    CommentUser=models.CharField(max_length=20)
    context=models.TextField()
    CommentTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.CommentedArticle.title


class SecnodComment(models.Model):
    SecnodCommentContext=models.ForeignKey(ArticleComment,on_delete=models.CASCADE)
    CommentUser = models.CharField(max_length=20)
    context = models.TextField()
    CommentTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.SecnodCommentContext.context