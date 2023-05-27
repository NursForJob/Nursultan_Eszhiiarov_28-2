import datetime

from django.shortcuts import HttpResponse, redirect

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == "GET":
        current_date = datetime.datetime.now()
        return HttpResponse(f'Date: {current_date}')


def good_bye(request):
    if request.method == "GET":
        return HttpResponse('Goodby user!')
