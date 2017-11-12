# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'website/home.html')

def captain(request):
    return render(request, 'website/captain.html')

def player(request):
    return render(request, 'website/player.html')