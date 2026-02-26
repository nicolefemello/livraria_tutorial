from rest_framework.viewsets import ModelViewSet

from core.models import Author
from core.serializers import AuthorSeriazlizer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSeriazlizer
