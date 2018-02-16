from django.db import models
from django.contrib.auth.models import User
from . import fields

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(User)
    song_file = models.FileField()
    time_posted = models.TimeField()

class Music_Video(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(User)
    video_file = models.FileField()
    time_posted = models.TimeField()

class Image(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(User)
    image_file = models.FileField()
    time_posted = models.TimeField()

class Story(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(User)
    text = models.TextField()
    time_posted = models.TimeField()

class Poem(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(User)
    text = models.TextField()
    time_posted = models.TimeField()

class Feedback(models.Model):
    owner = models.ForeignKey(User)
    ratings = fields.IntegerRangeField(min_value=0, max_value=5)
    comment = models.TextField()
    time_posted = models.TimeField()
    song = models.ForeignKey(Song, default=None)
    music_video = models.ForeignKey(Music_Video, default=None)
    image = models.ForeignKey(Image, default=None)
    story = models.ForeignKey(Story, default=None)
    poem = models.ForeignKey(Poem, default=None)
