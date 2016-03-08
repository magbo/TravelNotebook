from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Post

tags = ['restaurant', 'hostel', 'highlight', 'nature']


def index(request):
    return render(request, 'main/index.html', {})


def new_note(request):
    return render(request, 'main/new_note.html', {})


def new_link(request):
    return render(request, 'main/new_link.html', {})


def new_photo(request):
    return render(request, 'main/new_photo.html', {})


def post_list(request):
    return render(request, 'main/post_list.html', {})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'main/post_detail.html', {'post': post})



def tag_detail(request, tag):
    if str(tag).lower() in tags:
        #return HttpResponse('here is a list of tags for %s tag.' % tag)
        return render(request, 'main/tag_detail.html', {'tag': tag})
    else:
        raise Http404("This tag does not exist!!!!")


def tags_list(request):
    all_tags = tags
    return render(request, 'main/tags_list.html', {'all_tags': all_tags})


def show_trips(request):
    list_of_trips = Trip.objects.order_by('title')
    context = {'list_of_trips': list_of_trips}
    return render(request, 'main/show_trips.html', context)


def trip_detail(request, trip_id):
    try:
        trip = Trip.objects.get(pk=trip_id)
    except Trip.DoesNotExist:
        raise Http404("Trip does not exist")
    return render(request, 'main/trip_detail.html', {'trip': trip})
