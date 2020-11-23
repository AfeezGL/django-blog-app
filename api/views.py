from django.contrib.auth.models import User, Group
from article.models import Article
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import ArticleSerializer, LoginSerializer, UserSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Articles to be viewed.
    """
    queryset = Article.objects.all().order_by('-update_date')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for updating and deleting Articles
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class LoginApiView(generics.GenericAPIView):
    """
    API endpoint that allows Users to login and get authentication token so that they can create Articles
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })