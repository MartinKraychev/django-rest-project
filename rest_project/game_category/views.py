from django.shortcuts import render
from rest_framework.generics import ListAPIView

from rest_project.game_category.models import Category
from rest_project.game_category.serializers import ShowCategorySerializer


class ListCategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ShowCategorySerializer
