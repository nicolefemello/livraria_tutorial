from rest_framework.viewsets import ModelViewSet

from core.models import Book
from core.serializers import BookSeriazlizer, BookListSerializer, BookRetrieveSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSeriazlizer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookRetrieveSerializer
        return BookSeriazlizer
