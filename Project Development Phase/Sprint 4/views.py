# importing required packages

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from diab_retina_app import process


@csrf_exempt
def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

def abstract(request):
    if request.method == 'GET':
        return render(request, 'abstract.html')


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        response = process.process_img(img)
        return HttpResponse(response, status=200)
