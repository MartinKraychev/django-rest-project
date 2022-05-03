from django.contrib import admin

from rest_project.game.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'username')

    def username(self, obj):
        return obj.user.username
