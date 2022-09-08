from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'p1', 'p2', 'p3', 'sources')
        model = Article