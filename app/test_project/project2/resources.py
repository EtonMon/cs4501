# from tastypie.resources import ModelResource
# from project2.models import Song
# from tastypie.authorization import Authorization

# class SongResource(ModelResource):
#     class Meta:
#         queryset = Song.objects.all()
#         resource_name = 'song'
#         authorization = Authorization()
#         fields = ('id', 'title', 'artists', 'time_posted')