from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from petshow.views import *


class TestUrls(SimpleTestCase):
    def test_base_url(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
