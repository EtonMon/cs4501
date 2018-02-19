from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):

	class Meta:
		model = Song
		fields = ('id', 'title', 'artists', 'time_posted')
		read_only_fields = ('time_posted', 'time_posted')