from rest_framework import serializers
from .models import Song, Image, Story, Feedback, Music_Video, Poem, Custom_User
from . import models

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artists', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'artists', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'artists', 'text', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'ratings', 'comment', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class Music_Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Video
        fields = ('id', 'title', 'artists', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class Poem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('id', 'title', 'artists', 'text', 'time_posted', 'owner')
        read_only_fields = ('time_posted', 'time_posted')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ('id', 'username', 'password','first_name', 'last_name', 'date_created')
        read_only_fields = ('date_created', 'date_created')

class AuthenticatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Authenticator
        fields = ('user_id', 'authenticator')
        read_only_fields = ('date_created', 'date_created')

class SparkEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spark_Entries
        fields = ('item_id', 'recommended_items')