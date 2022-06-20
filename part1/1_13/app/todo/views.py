from time import time
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import shutil
import os
import datetime

import requests

from .forms import TodoForm





image_path = 'media/image.png'


def home(request):
    """Homepage for todo app"""
    get_image()
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TodoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TodoForm()

    return render(request, 'home.html', {'image_src':image_path, 'form': form})


def get_image():
    """Get image from picsum and save to file"""
    refresh_img = False
    try:
        img_timestamp = get_image_datetime()
        refresh_img = check_img_refresh(img_timestamp)
    except FileNotFoundError:
        print('no image found')
        refresh_img = True
    
    if refresh_img:
        # Refresh image by API request
        print('Requesting new image...')
        response = requests.get('https://picsum.photos/1200', stream=True)
        store_image(response.raw)
    else:
        print('No need to refresh, image is new')
    


def store_image(raw_image):
    """Store image in file"""
    with open(image_path, 'wb') as f:
        shutil.copyfileobj(raw_image, f)


def get_image_datetime():
    """Get modified time of image"""
    raw_time = os.path.getmtime(image_path)
    modified = datetime.datetime.fromtimestamp(raw_time)
    print('Modified:', modified)
    return modified

    #raw_time = os.path.getctime(image_path)
    #created = datetime.datetime.fromtimestamp(raw_time)
    #print('Created:', created)


def check_img_refresh(img_timestamp):
    """Check if image is one day old an needs a refresh
    True: Refresh
    False: Do not refresh
    """
    print(f'image timestamp: {img_timestamp}')
    print(f'timestamp now: {datetime.datetime.now()}')
    timedelta = datetime.datetime.now() - img_timestamp
    time_in_s = timedelta.total_seconds()
    days  = divmod(time_in_s, 86400)[0]
    print(f'image time difference: {days}')
    if days > 0:
        return True
    return False