from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
#from example_data.py import posts

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
    return HttpResponse('This is a post %s.' % post_id)


def tag_detail(request, tag_id):
    if str(tag_id).lower() in tags:
        return HttpResponse('here is a list of tags for %s tag.' % tag_id)
    else:
        raise Http404("This tag does not exist!!!!")


def tags_list(request):
    all_tags = tags
    return render(request, 'main/tags_list.html', {})
