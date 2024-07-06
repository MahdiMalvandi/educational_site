from rest_framework import serializers
from .models import Category


class GetCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'children', 'parent']


    def get_children(self, instance: Category):
        if instance.children.exists() is not None:
            return GetCategorySerializer(instance.children.all(), many=True).data
        else:
            return None


class CreateCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    parent = serializers.IntegerField(help_text="باید ایدی والد رو ارسال کنند", allow_null=True)

    def validate_slug(self, value):
        """Validating slug for category"""
        try:
            Category.objects.get(slug=value)
            raise serializers.ValidationError('A category with a slug already exists')
        except Category.DoesNotExist:
            return value

    def validate_parent(self, value=None):
        """Validate parent"""
        if value is not None:
            try:
                Category.objects.get(id=value)
                return value
            except Category.DoesNotExist:
                raise serializers.ValidationError("There isn't any category with this id")
        else:
            return None
