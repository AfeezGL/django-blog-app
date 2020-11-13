from django.contrib.auth.models import User, Group
from article.models import Article
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import ArticleSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Articles to be viewed.
    """
    queryset = Article.objects.all().order_by('-update_date')
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]