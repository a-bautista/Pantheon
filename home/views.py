from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
import requests

# main URL from the API
URL = "http://reminiscent-steady-albertosaurus.glitch.me/"

def index(request):
    if request.method == 'GET':
        try:
            template_name = 'home/index.html'
            
            noun   = str(URL)+'noun'
            verb   = str(URL)+'verb'
            adjective = str(URL)+'adjective'

            # Fetch the API and do deserialization
            responseNoun = requests.get(noun).json()
            responseVerb = requests.get(verb).json()
            responseAdjective = requests.get(adjective).json()

            context = {
                "sentence": ["My", "beautiful", "<noun>", "and", "I", "decided", "to", "<verb>", "together", "in", "this", "<adjective>", "day."], 
                "noun": responseNoun,
                "verb": responseVerb,
                "adjective": responseAdjective
            }
        except HttpResponseNotFound:
            return HttpResponseNotFound("Page not found")

    return render(request, template_name, context)



