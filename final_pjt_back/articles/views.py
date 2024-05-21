from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    print(request.user)
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' and article.user == request.user:
        my_dict = {'delete' : f'게시글 {article.title}을/를 삭제했습니다.'}
        article.delete()
        return Response(my_dict)

    elif request.method == 'PUT' and article.user == request.user:
        print('hi')
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def article_comments(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_comments_detail(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "PUT" and comment.user == request.user:
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE" and comment.user == request.user:
        my_dict = {'delete' : f'댓글 {comment.content}을/를 삭제했습니다.'}
        comment.delete()
        return Response(my_dict)
