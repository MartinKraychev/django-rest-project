from django.db import models


class Category(models.Model):
    CATEGORY_MAX_LENGTH = 20
    name = models.CharField(
        max_length=CATEGORY_MAX_LENGTH
    )

    description = models.TextField(
        blank=True,
        null=True,
    )
