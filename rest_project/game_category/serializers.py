from rest_framework.serializers import ModelSerializer

from rest_project.game_category.models import Category


class ShowCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
