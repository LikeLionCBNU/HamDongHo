from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

# BaseUserManager를 상속 받아 user와 superuser의 클래스를 오버라이딩
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username,)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, username, password):
        # username, password로 등록
        user = self.create_user(
            password=password,
            username=username,
        )
        # superuser에게 권한 부여
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=8, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    # 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
    
    # is_staff메소를 만들어주지 않으면 관리자일 때 동작해야할 동작들이 작동안할 수 있는건 해결
    @property
    def is_staff(self):
        return self.is_superuser

    # 사용자 고유 구분을 위함
    USERNAME_FIELD = 'username'

    # 필수는 아니지만 입력받고 싶을걸 추가한것.
    REQUIRED_FIELD = ['email']

    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    group = models.TextField(max_length=255, blank=True)