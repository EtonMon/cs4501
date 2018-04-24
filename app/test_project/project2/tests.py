from django.contrib.gis.geos import factory
from django.test import TestCase
import json
import uuid
from rest_framework.test import APITestCase
from .models import Song, Image, Story, Feedback, Music_Video, Poem, Custom_User, Authenticator
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .views import SongDetailsView, ImageDetailsView, StoryDetailsView, FeedbackDetailsView, Music_Video_DetailsView, Poem_DetailsView, CustomUserDetailsView

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
        """Test song creation capability."""
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
        """Test image creation capability."""
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
        """Test poem creation capability."""
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
        """Test music video creation capability."""
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
        """Test story creation capability."""
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
        """Test custom_user creation capability."""
        old_count = Custom_User.objects.count()
        self.object.save()
        new_count = Custom_User.objects.count()
        self.assertNotEqual(old_count, new_count)
        # self.assertEqual(self.object.status_code, status.HTTP_201_CREATED)

    def test_string_representation(self):
        """test Custom User __str__() returns the title """
        object = Custom_User(username="12jj42jer")
        self.assertEqual(str(object), object.username)


class FeedbackTestCase(TestCase):
    def setUp(self):
        """Define the custom_user instance and other test variables."""
        self.ratings = 5
        self.comment = "Awesome"
        user = Custom_User.objects.create(username="user1", first_name="tom", last_name="jerry")
        self.owner = user
        self.object = Feedback(ratings=self.ratings, comment=self.comment, owner=self.owner)

    def test_model_can_create_feedback(self):
        """Test feedback creation capability."""
        old_count = Feedback.objects.count()
        self.object.save()
        new_count = Feedback.objects.count()
        self.assertNotEqual(old_count, new_count)
        # self.assertEqual(self.object.status_code, status.HTTP_201_CREATED)

    def test_string_representation(self):
        """test feedback __str__() returns the ratings """
        object = Feedback(ratings=4)
        self.assertEqual(str(object), str(object.ratings))

class SongAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.song_data = {'title': 'No Promises', 'artists': 'Cheat Codes', 'owner': user.id}
        self.response = self.client.post(
            reverse('create_song'),
            self.song_data,
            format="json")

    def test_api_can_create_a_song(self):
        """POST: Test the api has song creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_song(self):
        """GET: Test the api can get a given song."""
        song = Song.objects.get()
        response = self.client.get(
            reverse('song_details',
            kwargs={'pk': song.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, song)

    def test_api_can_update_song(self):
        """PUT: Test the api can update a given song."""
        song = Song.objects.get()
        change_song = {'title': 'Something new', 'artists': 'Something new again...'}
        res = self.client.put(
            reverse('song_details', kwargs={'pk': song.id}),
            change_song, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Song.objects.get().title, 'Something new')
        self.assertEqual(Song.objects.get().artists, 'Something new again...')

    def test_api_can_delete_song(self):
        """DELETE: Test the api can delete a song."""
        song = Song.objects.get()
        response = self.client.delete(
            reverse('song_details', kwargs={'pk': song.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class ImageAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.image_data = {'title': 'No Promises', 'artists': 'Cheat Codes', 'owner': user.id}
        self.response = self.client.post(
            reverse('create_image'),
            self.image_data,
            format="json")

    def test_api_can_create_an_image(self):
        """POST: Test the api has image creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.get().title, 'No Promises')
        self.assertEqual(Image.objects.get().artists, 'Cheat Codes')

    def test_api_can_get_an_image(self):
        """GET: Test the api can get a given image."""
        image = Image.objects.get()
        response = self.client.get(
            reverse('image_details',
            kwargs={'pk': image.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, image)

    def test_api_can_update_image(self):
        """PUT: Test the api can update a given image."""
        image = Image.objects.get()
        change_image = {'title': 'Something new', 'artists': 'Something new again...'}
        res = self.client.put(
            reverse('image_details', kwargs={'pk': image.id}),
            change_image, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.get().title, 'Something new')
        self.assertEqual(Image.objects.get().artists, 'Something new again...')

    def test_api_can_delete_image(self):
        """DELETE: Test the api can delete an image."""
        image = Image.objects.get()
        response = self.client.delete(
            reverse('image_details', kwargs={'pk': image.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_images(self):
        """GET: Test the api can get all images."""
        image = Image.objects.get()
        response = self.client.get(
            reverse('image_list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, image)

class StoryAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.story_data = {'title': 'No Promises', 'artists': 'Cheat Codes', 'owner': user.id, 'text': 'hi there'}
        self.response = self.client.post(
            reverse('create_story'),
            self.story_data,
            format="json")

    def test_api_can_create_a_story(self):
        """POST: Test the api has story creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.get().title, 'No Promises')
        self.assertEqual(Story.objects.get().artists, 'Cheat Codes')

    def test_api_can_get_a_story(self):
        """GET: Test the api can get a given story."""
        story = Story.objects.get()
        response = self.client.get(
            reverse('story_details',
            kwargs={'pk': story.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, story)

    def test_api_can_update_story(self):
        """PUT: Test the api can update a given story."""
        story = Story.objects.get()
        change_story = {'title': 'Something new', 'artists': 'Something new again...', 'text': 'updating story'}
        res = self.client.put(
            reverse('story_details', kwargs={'pk': story.id}),
            change_story, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Story.objects.get().title, 'Something new')
        self.assertEqual(Story.objects.get().artists, 'Something new again...')
        self.assertEqual(Story.objects.get().text, 'updating story')

    def test_api_can_delete_story(self):
        """DELETE: Test the api can delete a story."""
        story = Story.objects.get()
        response = self.client.delete(
            reverse('story_details', kwargs={'pk': story.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_stories(self):
        """GET: Test the api can get all stories."""
        story = Story.objects.get()
        response = self.client.get(
            reverse('story_list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, story)

class Music_VideoAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.music_video_data = {'title': 'No Promises', 'artists': 'Cheat Codes', 'owner': user.id}
        self.response = self.client.post(
            reverse('create_music_video'),
            self.music_video_data,
            format="json")

    def test_api_can_create_a_music_video(self):
        """POST: Test the api has music video creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Music_Video.objects.get().title, 'No Promises')
        self.assertEqual(Music_Video.objects.get().artists, 'Cheat Codes')

    def test_api_can_get_a_music_video(self):
        """GET: Test the api can get a given music video."""
        music_video = Music_Video.objects.get()
        response = self.client.get(
            reverse('music_video_details',
            kwargs={'pk': music_video.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, music_video)

    def test_api_can_update_music_video(self):
        """PUT: Test the api can update a given music video."""
        music_video = Music_Video.objects.get()
        change_music_video = {'title': 'Something new', 'artists': 'Something new again...'}
        res = self.client.put(
            reverse('music_video_details', kwargs={'pk': music_video.id}),
            change_music_video, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Music_Video.objects.get().title, 'Something new')
        self.assertEqual(Music_Video.objects.get().artists, 'Something new again...')

    def test_api_can_delete_music_video(self):
        """DELETE: Test the api can delete a music video."""
        music_video = Music_Video.objects.get()
        response = self.client.delete(
            reverse('music_video_details', kwargs={'pk': music_video.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_music_videos(self):
        """GET: Test the api can get all music videos."""
        music_video = Music_Video.objects.get()
        response = self.client.get(
            reverse('music_video_list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, music_video)

class PoemAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.poem_data = {'title': 'No Promises', 'artists': 'Cheat Codes', 'owner': user.id}
        self.response = self.client.post(
            reverse('create_poem'),
            self.poem_data,
            format="json")

    def test_api_can_create_a_poem(self):
        """POST: Test the api has poem creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poem.objects.get().title, 'No Promises')
        self.assertEqual(Poem.objects.get().artists, 'Cheat Codes')

    def test_api_can_get_a_poem(self):
        """GET: Test the api can get a given poem."""
        poem = Poem.objects.get()
        response = self.client.get(
            reverse('poem_details',
            kwargs={'pk': poem.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, poem)

    def test_api_can_update_poem(self):
        """PUT: Test the api can update a given poem."""
        poem = Poem.objects.get()
        change_poem = {'title': 'Something new', 'artists': 'Something new again...'}
        res = self.client.put(
            reverse('poem_details', kwargs={'pk': poem.id}),
            change_poem, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Poem.objects.get().title, 'Something new')
        self.assertEqual(Poem.objects.get().artists, 'Something new again...')

    def test_api_can_delete_poem(self):
        """DELETE: Test the api can delete a poem."""
        poem = Poem.objects.get()
        response = self.client.delete(
            reverse('poem_details', kwargs={'pk': poem.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_poems(self):
        """GET: Test the api can get all poems."""
        poem = Poem.objects.get()
        response = self.client.get(
            reverse('poem_list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, poem)

class Custom_UserAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.custom_user_data = {'first_name': 'Promises', 'last_name': 'Cheat', 'username': 'user12'}
        self.response = self.client.post(
            reverse('create_custom_user'),
            self.custom_user_data,
            format="json")

    def test_api_can_create_a_custom_user(self):
        """POST: Test the api has custom user creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Custom_User.objects.get().first_name, 'Promises')
        self.assertEqual(Custom_User.objects.get().last_name, 'Cheat')
        self.assertEqual(Custom_User.objects.get().username, 'user12')

    def test_api_can_get_a_custom_user(self):
        """GET: Test the api can get a given custom user."""
        custom_user = Custom_User.objects.get()
        response = self.client.get(
            reverse('custom_user_details',
            kwargs={'pk': custom_user.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, custom_user)

    def test_api_can_update_custom_user(self):
        """PUT: Test the api can update a given custom user."""
        custom_user = Custom_User.objects.get()
        change_custom_user = {'first_name': 'Bob', 'last_name': 'Billy', 'username': 'user12000'}
        res = self.client.put(
            reverse('custom_user_details', kwargs={'pk': custom_user.id}),
            change_custom_user, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Custom_User.objects.get().first_name, 'Bob')
        self.assertEqual(Custom_User.objects.get().last_name, 'Billy')
        self.assertEqual(Custom_User.objects.get().username, 'user12000')

    def test_api_can_delete_custom_users(self):
        """DELETE: Test the api can delete a custom user."""
        custom_user = Custom_User.objects.get()
        response = self.client.delete(
            reverse('custom_user_details', kwargs={'pk': custom_user.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_all_custom_users(self):
        """GET: Test the api can get all users."""
        user = Custom_User.objects.get()
        response = self.client.get(
            reverse('custom_user_list'), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    #was trying to figure out how to create a user and authenticator separately and link the two...what I tried didn't work so well.

class Authenticator_UserAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.authen = uuid.uuid4()
        self.authenticator_data = {'user_id': 4, 'authenticator': self.authen}
        self.response = self.client.post(
            reverse('create_authenticator'),
            self.authenticator_data,
            format="multipart")

    def test_api_can_create_authenticator(self):
        """POST: Test the api has custom user creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Authenticator.objects.get().user_id, 4)
        self.assertEqual(Authenticator.objects.get().authenticator, self.authen)

    def test_api_can_get_authenticator(self):
        auth = Authenticator.objects.get()

        response = self.client.get(
            reverse('retrieve_authenticator',
            kwargs={'user_id': auth.user_id}), format="multipart")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, auth.user_id)

    def test_api_can_delete_authenticator(self):
        """DELETE: Test the api can delete a custom user."""
        auth = Authenticator.objects.get()
        print(auth.user_id)
        response = self.client.delete(
            reverse('retrieve_authenticator', kwargs={'user_id': auth.user_id}),
            format='multipart',
            follow=True)


class FeedbackAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = Custom_User.objects.create(username="user12", first_name="tom", last_name="jerry")
        self.feedback_data = {'ratings': 2, 'comment': 'this site is ok', 'owner': user.id}
        self.response = self.client.post(
            reverse('create_feedback'),
            self.feedback_data,
            format="json")

    def test_api_can_create_a_feedback(self):
        """POST: Test the api has feedback creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.get().ratings, 2)
        self.assertEqual(Feedback.objects.get().comment, 'this site is ok')

    def test_api_can_get_a_feedback(self):
        """GET: Test the api can get a given feedback."""
        feedback = Feedback.objects.get()
        response = self.client.get(
            reverse('feedback_details',
            kwargs={'pk': feedback.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, feedback)

    def test_api_can_update_feedback(self):
        """PUT: Test the api can update a given feedback."""
        feedback = Feedback.objects.get()
        change_feedback = {'ratings': 5, 'comment': 'Awesome.'}
        res = self.client.put(
            reverse('feedback_details', kwargs={'pk': feedback.id}),
            change_feedback, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Feedback.objects.get().ratings, 5)
        self.assertEqual(Feedback.objects.get().comment, 'Awesome.')

    def test_api_can_delete_feedback(self):
        """DELETE: Test the api can delete a feedback."""
        feedback = Feedback.objects.get()
        response = self.client.delete(
            reverse('feedback_details', kwargs={'pk': feedback.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
