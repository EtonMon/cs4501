from django.db import models
from django.contrib.auth.models import User

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

class Feedback(models.Model):
    owner = models.ForeignKey(User)
    ratings = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
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
