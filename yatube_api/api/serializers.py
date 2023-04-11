from rest_framework.serializers import ModelSerializer, SlugRelatedField

from posts.models import Comment, Group, Post


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "group", "pub_date")


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        read_only_fields = ("post",)
