from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='index'),
    path('create/', views.article_create, name='create'),
    path('<int:article_pk>/', views.article_detail, name='detail'),
    path('<int:article_pk>/likes/', views.article_like, name='likes'),
    path('<int:article_pk>/comments/', views.article_comments, name='comments_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/',
        views.article_comments_detail,
        name='comments_detail',
    ),
]
