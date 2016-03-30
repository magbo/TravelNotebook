from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Tag, Post
from .forms import TripForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, 'main/index.html', {})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_tags = post.tags.all()
    return render(request, 'main/post_detail.html', {'post': post, 'post_tags': post_tags})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('main:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_new.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('main:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_new.html', {'form': form})

@login_required
def posts_show(request):
    return render(request, 'main/posts_show.html', {})

@login_required
def trips_show(request):
    list_of_trips = Trip.objects.filter(owner=request.user).order_by('title')
    context = {'list_of_trips': list_of_trips}
    return render(request, 'main/trips_show.html', context)

@login_required
def trip_detail(request, pk): 
    trip = get_object_or_404(Trip, pk=pk)
    trip_posts = trip.post_set.all
    return render(request, 'main/trip_detail.html', {'trip': trip, 'trip_posts': trip_posts, })

@login_required
def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save()
            return redirect('main:trip_detail', pk=trip.pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'main/trip_new.html', {'form': form})

@login_required
def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST, owner=request.user)
        if form.is_valid():
            trip = form.save() 
            return redirect('main:trip_detail', pk=trip.pk)
    else:
        form = TripForm(owner=request.user)
    return render(request, 'main/trip_new.html', {'form': form})

@login_required
def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, value=tag_name)
    posts = tag.post_set.all
    return render(request, 'main/tag_detail.html', {'tag': tag, 'posts': posts})

@login_required
def tags_show(request):
    tags = Tag.objects.order_by('value')
    return render(request, 'main/tags_show.html', {'tags': tags})





