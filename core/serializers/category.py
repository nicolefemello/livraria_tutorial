from rest_framework.serializers import ModelSerializer

from core.models import Category


class CategorySeriazlizer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
