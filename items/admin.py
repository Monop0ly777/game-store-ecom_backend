from django.contrib import admin
from .models import Items, Genres


# Register your models here.


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)



@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ("name", )
