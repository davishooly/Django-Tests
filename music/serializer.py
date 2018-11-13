from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class meta:
        models = Songs
        fields = ("title", "artist")