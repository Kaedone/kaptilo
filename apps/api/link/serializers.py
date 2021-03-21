from rest_framework import serializers

from apps.link import models

__all__ = ["LinkCreateSerializer", "LinkListSerializer", "LinkRetrieveSerializer", "LinkUpdateSerializer"]


class LinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = ["id", "link", "uses", "shortened", "created"]
        read_only_fields = ["id", "uses", "shortened", "created"]


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = ["id", "link", "uses", "shortened", "created"]


class LinkRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = ["id", "link", "uses", "shortened", "created"]


class LinkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = ["id", "link", "uses", "shortened", "created"]
        read_only_fields = ["id", "uses", "shortened", "created"]
