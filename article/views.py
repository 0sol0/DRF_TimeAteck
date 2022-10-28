from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
