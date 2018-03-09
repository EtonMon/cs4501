from django.contrib import admin
from .models import Song, Music_Video, Image, Story, Poem, Feedback

# Register your models here.
admin.site.register(Song)
admin.site.register(Music_Video)
admin.site.register(Image)
admin.site.register(Story)
admin.site.register(Poem)
admin.site.register(Feedback)
