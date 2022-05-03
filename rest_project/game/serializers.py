from rest_framework.serializers import ModelSerializer

from rest_project.game.models import Game


class DetailsGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class ListGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'image', 'category')


class CreateGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'image', 'summary', 'category')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
