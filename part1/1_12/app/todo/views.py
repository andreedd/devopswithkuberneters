from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import shutil
import os
import datetime

import requests

image_path = 'images/image.png'

def home(request):
    """Homepage for todo app"""
    image = get_image()
    return render(request, 'home.html')


def get_image():
    """Get image from picsum and save to file"""
    response = requests.get('https://picsum.photos/1200', stream=True)
    store_image(response.raw)
    get_image_datetime()


def store_image(raw_image):
    with open(image_path, 'wb') as f:
        shutil.copyfileobj(raw_image, f)


def get_image_datetime():
    raw_time = os.path.getmtime(image_path)
    modified = datetime.datetime.fromtimestamp(raw_time)
    print('Modified:', modified)

    raw_time = os.path.getctime(image_path)
    created = datetime.datetime.fromtimestamp(raw_time)
    print('Created:', created)