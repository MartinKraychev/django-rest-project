from django.contrib import admin

from rest_project.furniture.models import Furniture


@admin.register(Furniture)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')

    def username(self, obj):
        return obj.user.username
