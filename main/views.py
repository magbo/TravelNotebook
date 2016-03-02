from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the main site of my travel app")

def new_note(request):
    return HttpResponse("Here you can add a new note")

def new_link(request):
    return HttpResponse("Here you can add a new link")

def new_photo(request):
    return HttpResponse("Add a new photo here")

def post_list(request):
    return HttpResponse("list of all posts")


# Create your views here.
