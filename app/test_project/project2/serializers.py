from rest_framework import serializers
from .models import Song, Music_Video, Poem

class SongSerializer(serializers.ModelSerializer):

	class Meta:
		model = Song
		fields = ('id', 'title', 'artists', 'time_posted')
		read_only_fields = ('time_posted', 'time_posted')

class Music_Video_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Music_Video
		fields = ('id', 'title', 'artists', 'time_posted')
		read_only_fields = ('time_posted', 'time_posted')

class Poem_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Poem
		fields = ('id', 'title', 'artists', 'time_posted')
		read_only_fields = ('time_posted', 'time_posted')