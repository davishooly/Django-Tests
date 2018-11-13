from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Songs


class BaseViewTest(APIClient):

    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        # add test data
        self.create_song("on the top", "kimame")
        self.create_song("noma noma", "Dryspell")


class GetAllSongs(BaseViewTest):
    def test_get_all_songs(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"}))

        expected = Songs.objects.all()


# Create your tests here.
