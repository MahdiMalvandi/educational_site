from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.permissions import TeacherOrAdmins, OnlySuperUser

from .models import Category
from .serializers import *


class CategoryViewSet(ModelViewSet):
    serializers = GetCategorySerializer
    queryset = Category.objects.exclude(parent__isnull=False)
    lookup_field = 'slug'
    pagination_class = None

    permission_classes_per_method = {
        "list":  None,
        "retrieve": None,
        "create": [TeacherOrAdmins],
        "update": [TeacherOrAdmins],
        "delete": [OnlySuperUser]

    }
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateCategorySerializer
        return GetCategorySerializer


