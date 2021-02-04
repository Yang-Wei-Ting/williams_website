from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):
    # views
    def test_home_view(self):
        response = self.client.get(
            reverse('home'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertEqual(response.context['greeting_msg'], '')

        response = self.client.get(
            reverse('home'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertEqual(response.context['greeting_msg'], 'Welcome Back!')
