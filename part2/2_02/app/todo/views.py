from time import time
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

import shutil
import os
import datetime
import json

import requests

from .models import Todo


image_path = 'media/image.png'

# "/" endpoint
def image(request):
    """Basic endpoint for todo app"""
    get_image()
    return JsonResponse({'img_path': image_path})


# "/todos" endpoint
def todos(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        todo = body['todo']
        print(f'added todo: {todo}')
        Todo(title=todo).save()
        todos = list(Todo.objects.all().values('title', 'id'))
        return JsonResponse({'data': todos})
    todos = list(Todo.objects.all().values('title', 'id'))
    print(f'returning todos: {todos}')
    return JsonResponse({'data': todos})


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