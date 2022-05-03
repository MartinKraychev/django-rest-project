from django.contrib.auth import get_user_model
from django.db import models

from rest_project.game_category.models import Category

UserModel = get_user_model()


class Game(models.Model):
    title = models.CharField(
        max_length=40
    )

    image = models.URLField()

    summary = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'
