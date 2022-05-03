from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from rest_project.game.models import Game
from rest_project.game.serializers import ListGameSerializer, CreateGameSerializer, DetailsGameSerializer


class CreateListGamesView(ListCreateAPIView):
    queryset = Game.objects.all()

    list_serializer = ListGameSerializer
    create_serializer = CreateGameSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer
        return self.list_serializer


class DetailsGameView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = DetailsGameSerializer
