from django.contrib import admin
from .models import ArticleType, article, ArticleComment


@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type')

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display = ('title','articletype','auth','CreateTime','ChangeTime','LookTime','CommentTime')


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('CommentUser','context','CommentTime')



