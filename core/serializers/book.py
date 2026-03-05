from rest_framework.serializers import ModelSerializer

from core.models import Book


class BookSeriazlizer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1


class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price')
