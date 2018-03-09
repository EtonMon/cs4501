from django.test import TestCase
from .models import Song
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):

	def setUp(self):
		self.song_title = "Root"
		self.artist = "Tom"
        # self.owner = 1
        # self.songfile = null
		self.song = Song(title=self.song_title, artists=self.artist)

	def test_model_can_create_a_song(self):
		old_count = Song.objects.count()
		self.song.save()
		new_count = Song.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.song_data = {'title': 'No Promises', 'artists': 'Cheat Codes'}
        self.response = self.client.post(
            reverse('create'),
            self.song_data,
            format="json")

    def test_api_can_create_a_song(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_song(self):
        """Test the api can get a given bucketlist."""
        song = Song.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': song.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, song)

    def test_api_can_update_song(self):
        """Test the api can update a given bucketlist."""
        song = Song.objects.get()
        change_song = {'title': 'Something new', 'artists': 'Something new again...'}
        res = self.client.put(
            reverse('details', kwargs={'pk': song.id}),
            change_song, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_song(self):
        """Test the api can delete a bucketlist."""
        song = Song.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': song.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)








