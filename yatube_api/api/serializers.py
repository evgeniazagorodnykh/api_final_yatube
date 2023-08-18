import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.shortcuts import get_object_or_404


from posts.models import Comment, Post, Group, Follow, User


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.CharField()

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')

    def create(self, validated_data):
        following = validated_data['following']
        user = validated_data['user']
        if following == str(user):
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя')
        if Follow.objects.filter(
                following__username=following, user=user).count() != 0:
            raise serializers.ValidationError(
                'Нельзя дважды подписаться на одного пользователя')
        cur_following = get_object_or_404(User, username=following)
        return Follow.objects.create(following=cur_following, user=user)
