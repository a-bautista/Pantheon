from django.test import TestCase, Client
from django.urls import reverse, resolve
from home.views import madlib
import requests
from rest_framework import status

class TestUrls(TestCase):

    def test_list_url_is_resolved(self):
        url = reverse('madlib')
        self.assertEquals(resolve(url).func, madlib)

    def test_api_url(self):
        url = "http://reminiscent-steady-albertosaurus.glitch.me/"
        nounR   = requests.get(str(url)+'noun')
        verbR   = requests.get(str(url)+'verb')
        adjectiveR = requests.get(str(url)+'adjective')

        self.assertEquals(nounR.status_code, status.HTTP_200_OK)
        self.assertEquals(verbR.status_code, status.HTTP_200_OK)
        self.assertEquals(adjectiveR.status_code, status.HTTP_200_OK)
        
    def test_madlib_view(self):
        client = Client()
        response = client.get(reverse('madlib'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/madlib.html')