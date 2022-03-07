from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserInfTable,muteuser
from django.contrib.auth.admin import UserAdmin as BaseAdmin


class UserInfTableInline(admin.TabularInline):
    model = UserInfTable
    can_delete = False
    verbose_name_plural = '普通用户信息'

class UserAdmin(BaseAdmin):
    inlines = (UserInfTableInline,)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)

@admin.register(muteuser)
class muteuserAdmin(admin.ModelAdmin):
    model = muteuser
    list_display = ('qqnumber','qqmessage1','qqmessage2','qqmessage3','qqmessagetimes','lastmessagedate')