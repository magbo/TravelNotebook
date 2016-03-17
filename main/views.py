from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Trip, Tag, Post
from .forms import TripForm, PostForm



def index(request):
    return render(request, 'main/index.html', {})


def posts_show(request):
    return render(request, 'main/posts_show.html', {})


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post_tags = post.tags.all()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'main/post_detail.html', {'post': post, 'post_tags': post_tags})


def tag_detail(request, tag_name):
    try:
        tag = Tag.objects.get(value=tag_name)
        posts = tag.post_set.all
   
        
    except Tag.DoesNotExist:
        raise Http404("This tag does not exist!!!!")
        #return HttpResponse('here is a list of tags for %s tag.' % tag)
    return render(request, 'main/tag_detail.html', {'tag': tag, 'posts': posts})


def tags_show(request):
    tags = Tag.objects.order_by('value')
    return render(request, 'main/tags_show.html', {'tags': tags})


def trips_show(request):
    list_of_trips = Trip.objects.order_by('title')
    context = {'list_of_trips': list_of_trips}
    return render(request, 'main/trips_show.html', context)


def trip_detail(request, pk): 
    try:
        trip = Trip.objects.get(pk=pk)
        trip_posts = trip.post_set.all
    except Trip.DoesNotExist:
        raise Http404("Trip does not exist")
    return render(request, 'main/trip_detail.html', {'trip': trip, 'trip_posts': trip_posts})


def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save() 
            return redirect('main:trip_detail', pk=trip.pk)
    else:
        form = TripForm()
        return render(request, 'main/trip_new.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save() 
            return redirect('main:post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'main/post_new.html', {'form': form})



