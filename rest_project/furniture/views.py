from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_project.furniture.models import Furniture
from rest_project.furniture.serializers import CreateListFurnitureSerializer


class CreateListFurnitureView(ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = CreateListFurnitureSerializer


class FurnitureDetailsView(RetrieveAPIView):
    queryset = Furniture.objects.all()
    serializer_class = CreateListFurnitureSerializer

