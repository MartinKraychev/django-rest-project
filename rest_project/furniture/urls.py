from django.urls import path

from rest_project.furniture.views import CreateListFurnitureView, FurnitureDetailsView

urlpatterns = (
    path('', CreateListFurnitureView.as_view(), name='dashboard'),
    path('<int:pk>/', FurnitureDetailsView.as_view(), name='details'),
)
