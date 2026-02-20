from rest_framework.viewsets import ModelViewSet

from core.models import Category
from core.serializers import CategorySeriazlizer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySeriazlizer
