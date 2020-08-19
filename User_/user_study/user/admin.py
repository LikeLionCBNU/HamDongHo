from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ExtraUserData
# Register your models here.

# 기본 모델 레이아웃을 선택해 ExtraUserData를 Admin에 추가
class ExtraInline(admin.StackedInline):
    model = ExtraUserData

# 메소드를 오버라이딩 해줌. display에 기존 것과 'date_joined'를 같이 표시
class MyUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['date_joined',]

    # ExtraUserData 를 넣어라!
    inlines = [
        ExtraInline,
    ]

# 기본적으로 user를 register하니깐 여기서 해재 하고 넣어 줘야함
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)