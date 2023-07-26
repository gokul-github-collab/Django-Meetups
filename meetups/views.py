from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Meetup

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {"meetups": meetups})


def details(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
        return render(request, "meetups/meetup-detail.html", {"meetup" : meetup, "meetup_found": True})
    except Exception as exc:
        return render(request, "meetups/meetup-detail.html", {"meetup_found": False})