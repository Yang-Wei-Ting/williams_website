from django.test import TestCase

from .models import HomeCaption


class HomeModelsTest(TestCase):
    def setUp(self):
        self.home_caption = HomeCaption.objects.create(
            purpose="purpose",
            text="text",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.home_caption), self.home_caption.purpose)
