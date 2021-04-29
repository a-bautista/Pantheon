from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import madlib
import requests, re

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('madlib')
        self.assertEquals(resolve(url).func, madlib)

    def test_api_url(self):
        url = "http://reminiscent-steady-albertosaurus.glitch.me/"
        noun   = str(url)+'noun'
        verb   = str(url)+'verb'
        adjective = str(url)+'adjective'

        responseNoun = re.search(r'\b200\b', str(requests.get(noun)))
        responseVerb = re.search(r'\b200\b', str(requests.get(verb)))
        responseAdjective = re.search(r'\b200\b', str(requests.get(adjective)))

        if responseAdjective and responseNoun and responseVerb:
            responseAPI = "OK"

        self.assertEquals(responseAPI, "OK")

