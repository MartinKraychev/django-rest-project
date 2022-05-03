from django.urls import path

from rest_project.game.views import CreateListGamesView, DetailsGameView

urlpatterns = (
    path('', CreateListGamesView.as_view(), name='dashboard'),
    path('<int:pk>/', DetailsGameView.as_view(), name='details'),
)
