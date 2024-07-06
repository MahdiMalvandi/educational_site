from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    slug = models.CharField(db_index=True, max_length=255, unique=True, verbose_name='اسلاگ')
    parent = models.ForeignKey("self", null=True, blank=True, related_name='children', on_delete=models.SET_NULL)


    class Meta:
        db_table = 'categories'
