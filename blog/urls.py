from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name = "post"),
    path('post/', views.PostList.as_view(), name='post'),
    path('post-detail/<pk>', views.PostDetail.as_view(), name='post-detail'),
    path('author', views.AuthorList.as_view(), name='author'),
    path('author-detail/<pk>', views.AuthorDetail.as_view(), name='author-detail'),
]

