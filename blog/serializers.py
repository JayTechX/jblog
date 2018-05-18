from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        #fields = ('post_name','post_message','post_author','post_img','post_date','post_highlight')
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        #fields = ('first_name','last_name','date_of_birth','date_of_death','author_img','author_description')
        fields = '__all__'