from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from rest_project.game.models import Game
from rest_project.game_category.serializers import ShowCategorySerializer


class DetailsGameSerializer(ModelSerializer):
    category = ShowCategorySerializer(many=False, )

    class Meta:
        model = Game
        fields = '__all__'


class ListGameSerializer(ModelSerializer):
    category = ShowCategorySerializer(many=False,)

    class Meta:
        model = Game
        fields = ('title', 'image', 'id', 'category')


class CreateGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'image', 'summary', 'category')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class UpdateGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'image', 'summary', 'category')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
