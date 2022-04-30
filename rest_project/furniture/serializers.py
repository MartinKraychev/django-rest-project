from rest_framework.serializers import ModelSerializer

from rest_project.furniture.models import Furniture


class CreateListFurnitureSerializer(ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
