from django.urls import path

from rest_project.game.views import CreateListGamesView, DetailsUpdateDeleteGameView

urlpatterns = (
    path('', CreateListGamesView.as_view(), name='create and list'),
    path('<int:pk>/', DetailsUpdateDeleteGameView.as_view(), name='details update and delete'),
)
