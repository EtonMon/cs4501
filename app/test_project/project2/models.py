from django.db import models
from django.contrib.auth.models import User
from . import fields


class Custom_User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.username)

    def __unicode__(self):
        return '%s' % (self.username)

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    # song_file = models.FileField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Music_Video(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    #video_file = models.FileField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Image(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    #image_file = models.FileField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Story(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    text = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Poem(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT_TITLE")
    artists = models.CharField(max_length=50, default="NO_ARTIST")
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    text = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

class Feedback(models.Model):
    owner = models.ForeignKey(Custom_User, default=1, on_delete=models.CASCADE)
    ratings = fields.IntegerRangeField(min_value=0, max_value=5)
    comment = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)
    # song = models.ForeignKey(Song, default=None)
    # music_video = models.ForeignKey(Music_Video, default=None)
    # image = models.ForeignKey(Image, default=None)
    # story = models.ForeignKey(Story, default=None)
    # poem = models.ForeignKey(Poem, default=None)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.ratings)

# class User(models.Model):
#     username = models.CharField(max_length=50, default="NO_NAME")
#     lastname = models.CharField(max_length=50, default="last_name")
#     firstname = models.CharField(max_length=50, default="first_name")
