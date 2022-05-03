from django.urls import path

from rest_project.game_category.views import ListCategoriesView

urlpatterns = (
    path('', ListCategoriesView.as_view(), name='categories'),
)
