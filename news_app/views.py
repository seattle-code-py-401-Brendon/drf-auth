from rest_framework import generics
from .serializer import ArticleSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
