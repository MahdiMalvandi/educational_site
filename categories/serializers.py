from rest_framework import serializers
from .models import Category


class GetCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'children']

    def get_children(self, instance: Category):
        return GetCategorySerializer(instance.children.all(), many=True).data


class CreateCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    slug = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)
    parent = serializers.IntegerField(help_text="باید ایدی والد رو ارسال کنند", allow_null=True, required=False)

    def validate_slug(self, value):
        """Validating slug for category"""
        try:
            Category.objects.get(slug=value)
            raise serializers.ValidationError({"error": 'A category with a slug already exists'})
        except Category.DoesNotExist:
            return value

    def validate_name(self, value):
        """Validating name for category"""
        try:
            Category.objects.get(name=value)
            raise serializers.ValidationError({"error": 'A category with a name already exists'})
        except Category.DoesNotExist:
            return value

    def validate_parent(self, value=None):
        """Validate parent"""
        if value is not None:
            try:
                Category.objects.get(id=value)
                return value
            except Category.DoesNotExist:
                raise serializers.ValidationError({"error": "There isn't any category with this id"})
        else:
            return None

    def create(self, validated_data):
        # Validate Name
        if validated_data.get('name', None) is None:
            raise serializers.ValidationError(detail={"error": "Name field is required."})

        # Create Slug if it doesn't exist
        if validated_data.get('slug', None) is None:
            slug_value = validated_data['name'].replace(' ', '-')
            self.validate_slug(slug_value)
        else:
            slug_value = validated_data.get('slug')

        # Create Object
        obj = Category.objects.create(name=validated_data['name'], parent=validated_data.get('parent', None),
                                      slug=slug_value)
        return obj

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
