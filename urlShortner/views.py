from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import urlShortner
from django.db.models import Q
from django.utils import timezone
import requests

# Create your views here.
def getshorturl(input_url,latest_id):
    #order_by - id, get last id for shortening
    encoding = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    BASE = len(encoding)
    codes = []

    while (latest_id > 0):
        codes.insert(0,latest_id % BASE)
        latest_id = latest_id/BASE

    encoded_url = ''.join([encoding[code] for code in codes])
    return "http://www.my-awesome-urlshortner.com/" + encoded_url

def externalURL(request,external_url):
    context = {}
    try:
        external_response = requests.get(external_url)
        context = {'external_response': external_response}
    except:
        context = {'external_response': []}
        return render(request, 'urlShortner/externalURL.html', context)

def index(request):
    if request.method == 'GET':
        return render(request, 'urlShortner/index.html', {})
    elif request.method == 'POST':
        input_url = request.POST['url']
        context = {}
        try:
	    search_url = urlShortner.objects.get(Q(shorturl=input_url) | 
                                                 Q(fullurl=input_url))
            if (input_url == search_url.fullurl):
                context = {'input_url': search_url.shorturl}
            elif (input_url == search_url.shorturl):
                context = {'input_url': search_url.fullurl}
        except:
            newurl = urlShortner(fullurl=input_url,
                                 entry_date=timezone.now())
            newurl.save()

            latest_id = newurl.id
            output_url = getshorturl(input_url,latest_id)
            newurl.shorturl = output_url
            newurl.save()

            context = {'input_url': output_url}
        return render(request, 'urlShortner/index.html', context)
