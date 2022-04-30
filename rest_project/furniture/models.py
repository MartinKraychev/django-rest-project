from django.contrib.auth import get_user_model
from django.db import models

from rest_project.category.models import Category

UserModel = get_user_model()


class Furniture(models.Model):
    name = models.CharField(
        max_length=20
    )

    image = models.URLField()

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'
