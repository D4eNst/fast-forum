from django.contrib import admin
from forum.models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class GameAdmin(admin.ModelAdmin):
    pass
