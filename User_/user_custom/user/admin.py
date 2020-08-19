from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.

# 기본 모델 레이아웃을 선택해 ExtraUserData를 Admin에 추가
class ExtraInline(admin.StackedInline):
    model = Profile

# 선언된 admin이 없기 때문에 admin.ModelAdmin이라는 뼈대를 가져와서 profile의 내용을 추가하는 것
class MyUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email')
    #list_filter = ('is_admin',)
    #def __init__(self, *args, **kwargs):
    #    super(CustomUser, self).__init__(*args, **kwargs)
    #    CustomUser.list_display = list(CustomUser.list_display) + ['group',]

    # ExtraUserData 를 넣어라!
    inlines = [
        ExtraInline,
    ]

# CustomUser는 admin으로 선언되어져 있는게 아니니까 굳이 unregister하지 않음
#admin.site.unregister(CustomUser)
admin.site.register(CustomUser, MyUserAdmin)