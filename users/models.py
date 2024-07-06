from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


def user_profile_upload_path(instance, filename):
    return f"profiles/{instance.username}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    username = models.CharField(max_length=32, unique=True, verbose_name="نام کاربری")
    email = models.EmailField(max_length=50, unique=True, verbose_name="ایمیل")
    profile = models.ImageField(upload_to=user_profile_upload_path, blank=True, null=True, verbose_name="پروفایل")
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    bio = models.TextField(null=True, blank=True, verbose_name="بیو")
    is_staff = models.BooleanField(default=False, verbose_name="ایا ادمین است")
    is_teacher = models.BooleanField(default=False, verbose_name="ایا مدرس است")
    is_superuser = models.BooleanField(default=False, verbose_name="ایا مدیر است")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'



