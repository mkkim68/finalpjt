from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='index'),
    path('articles/<int:article_pk>/', views.article_detail, name='detail'),
    path('articles/<int:article_pk>/likes/', views.article_like, name='likes'),
    path('articles/<int:article_pk>/comments/', views.article_comments_create, name='comments_create'),
    path(
        'articles/<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.article_comments_delete,
        name='comments_delete',
    ),
]
