from rest_framework import serializers

from wildberries.models import Product


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["article"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
