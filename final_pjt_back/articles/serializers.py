from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import CustomUserSerializer


class CommentListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__" 
        

class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('like_users',)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article')
