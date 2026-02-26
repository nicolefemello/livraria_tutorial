from rest_framework.serializers import ModelSerializer

from core.models import Publisher

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'