from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Meetup, Partcipant
from .forms import RegisterationForm
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {"meetups": meetups})


def details(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    try:
        if request.method == "GET":

            registration_form = RegisterationForm()
            return render(request, "meetups/meetup-detail.html", {"meetup": meetup, "meetup_found": True, "form": registration_form})
        else:
            registration_form = RegisterationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                partcipant, _ = Partcipant.objects.get_or_create(
                    email=user_email)
                meetup.participants.add(partcipant)
                return redirect("confirm-registration", slug=slug)
            else:
                return render(request, "meetups/meetup-detail.html", {"meetup": meetup, "meetup_found": True, "form": registration_form})

    except Exception as exc:
        print(exc)
        return render(request, "meetups/meetup-detail.html", {"meetup_found": False})


def confirm_registration(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, "meetups/registration-success.html", {"meetup": meetup})
