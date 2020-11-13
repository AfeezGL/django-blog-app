from article.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'image', 'title', 'body', 'slug', 'update_date', 'short_text']

