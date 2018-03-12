from django.test import TestCase
from .models import Song, Image, Story, Feedback, Music_Video, Poem, Custom_User
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class SongTestCase(TestCase):

    def setUp(self):
        """Define the song instance and other test variables."""
        self.title = "Root"
        self.artist = "Tom"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Song(title=self.title, artists=self.artist, owner=self.owner)

    def test_model_can_create_a_song(self):
        """Test the api has song creation capability."""
        old_count = Song.objects.count()
        self.object.save()
        new_count = Song.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test Song __str__() returns the title """
        object = Song(title="Alphabet Song")
        self.assertEqual(str(object), object.title)

class ImageTestCase(TestCase):
    def setUp(self):
        """Define the image instance and other test variables."""
        self.title = "Root"
        self.artist = "Tom"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Image(title=self.title, artists=self.artist, owner=self.owner)

    def test_model_can_create_a_image(self):
        """Test the api has image creation capability."""
        old_count =Image.objects.count()
        self.object.save()
        new_count = Image.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test Image __str__() returns the title """
        object = Image(title="Mona Lisa")
        self.assertEqual(str(object), object.title)

class PoemTestCase(TestCase):
    def setUp(self):
        """Define the poem instance and other test variables."""
        self.title = "Root"
        self.artist = "Tom"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Poem(title=self.title, artists=self.artist, owner=self.owner)

    def test_model_can_create_a_poem(self):
        """Test the api has poem creation capability."""
        old_count = Poem.objects.count()
        self.object.save()
        new_count = Poem.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test __str__() returns the title """
        object = Poem(title="The Roads Are Split")
        self.assertEqual(str(object), object.title)

class Music_VideoTestCase(TestCase):
    def setUp(self):
        """Define the music video instance and other test variables."""
        self.title = "Root"
        self.artist = "Tom"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Music_Video(title=self.title, artists=self.artist, owner=self.owner)

    def test_model_can_create_a_music_video(self):
        """Test the api has music video creation capability."""
        old_count = Music_Video.objects.count()
        self.object.save()
        new_count = Music_Video.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test Music Video __str__() returns the title """
        object = Music_Video(title="The Roads Are Split")
        self.assertEqual(str(object), object.title)

class StoryTestCase(TestCase):
    def setUp(self):
        """Define the story instance and other test variables."""
        self.title = "Root"
        self.artist = "Tom"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Story(title=self.title, artists=self.artist, owner=self.owner)

    def test_model_can_create_a_story(self):
        """Test the api has story creation capability."""
        old_count = Story.objects.count()
        self.object.save()
        new_count = Story.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test Story __str__() returns the title """
        object = Story(title="The Roads Are Split")
        self.assertEqual(str(object), object.title)

class Custom_UserTestCase(TestCase):
    def setUp(self):
        """Define the custom_user instance and other test variables."""
        self.first_name = "Tom"
        self.last_name = "Jerry"
        self.username = "TomJerry"
        self.object = Custom_User(first_name=self.first_name, last_name=self.last_name, username=self.username)

    def test_model_can_create_a_story(self):
        """Test the api has custom_user creation capability."""
        old_count = Custom_User.objects.count()
        self.object.save()
        new_count = Custom_User.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_string_representation(self):
        """test Custom User __str__() returns the title """
        object = Custom_User(username="12jj42jer")
        self.assertEqual(str(object), object.username)

# class ViewTestCase(TestCase):
#     """Test suite for the api views."""
#
#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.client = APIClient()
#         self.song_data = {'title': 'No Promises', 'artists': 'Cheat Codes'}
#         self.response = self.client.post(
#             reverse('create'),
#             self.song_data,
#             format="json")
#
#     def test_api_can_create_a_song(self):
#         """Test the api has bucket creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#
#     def test_api_can_get_a_song(self):
#         """Test the api can get a given bucketlist."""
#         song = Song.objects.get()
#         response = self.client.get(
#             reverse('details',
#             kwargs={'pk': song.id}), format="json")
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, song)
#
#     def test_api_can_update_song(self):
#         """Test the api can update a given bucketlist."""
#         song = Song.objects.get()
#         change_song = {'title': 'Something new', 'artists': 'Something new again...'}
#         res = self.client.put(
#             reverse('details', kwargs={'pk': song.id}),
#             change_song, format='json'
#         )
#         self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_api_can_delete_song(self):
    #     """Test the api can delete a bucketlist."""
    #     song = Song.objects.get()
    #     response = self.client.delete(
    #         reverse('details', kwargs={'pk': song.id}),
    #         format='json',
    #         follow=True)
    #
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
