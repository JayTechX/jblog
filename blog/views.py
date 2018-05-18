# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Author
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer,AuthorSerializer

# Api views
# api/posts
class PostApiList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# api/authors
class AuthorApiList(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)



# Create your views here.

class PostList(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()

    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    paginate_by = 10

    template_name = 'blog/post_detail.html'


class AuthorList(generic.ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()

    template_name = 'blog/author.html'


class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'blog/author_detail.html'
