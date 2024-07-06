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

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    profile = models.ImageField(upload_to=user_profile_upload_path, blank=True, null=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_seen = models.DateTimeField('last seen date', default=timezone.now)

    bio = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'



