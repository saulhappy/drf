from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fileds = ("id", "title", "author", "excerpt", "content", "status")
