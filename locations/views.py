from django.shortcuts import render

from django.views.generic import ListView

from locations.models import Location


class LocationView(ListView):
    model = Location