from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Items, Genres


class ItemsSerializer(serializers.ModelSerializer):
    # genres = serializers.PrimaryKeyRelatedField(queryset=Genres.objects.all(), many=True)
    genres = serializers.SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Items
        fields = "__all__"
