from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404


from .models import Trip, Tag, Post
from .forms import TripForm, PostForm

User = get_user_model()


def index(request):
    return render(request, 'main/index.html', {})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.trip.owner.id != request.user.id:
        raise Http404
    else: 
        post_tags = post.tags.all()
    return render(request, 'main/post_detail.html', {'post': post, 'post_tags': post_tags})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    trip = post.trip
    if post.trip.owner.id != request.user.id:
        raise Http404
    else: 
        post.delete()
    return redirect('main:trip_detail', pk=post.trip.pk)    


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.trip.owner.id != request.user.id:
        raise Http404
    else: 
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                messages.success(request, 'Saved!')
                return redirect('main:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    return render(request, 'main/post_new.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #form.trip.queryset = Trip.objects.filter(trip_owner=request.user.id)
        #form.fields["trip"].queryset = Trip.objects.filter(owner__trip=request.user)

        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post successfully created!')
            return redirect('main:post_detail', pk=post.pk)
        else:
            messages.error(request, 'Not created yet')    
    else:
        form = PostForm()
    return render(request, 'main/post_new.html', {'form': form})

@login_required
def posts_show(request):
    return render(request, 'main/posts_show.html', {})

@login_required
def trips_show(request):
    list_of_trips = Trip.objects.filter(owner=request.user).order_by('title')
    context = {
        'list_of_trips': list_of_trips
        }
    return render(request, 'main/trips_show.html', context)

@login_required
def trip_detail(request, pk): 
    trip = get_object_or_404(Trip, pk=pk)
    if trip.owner.id != request.user.id:
        raise Http404
    else:    
        trip_posts = trip.post_set.all().order_by('-created_date')
        paginator = Paginator(trip_posts, 1) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            trip_posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            trip_posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            trip_posts = paginator.page(paginator.num_pages)

    return render(request, 'main/trip_detail.html', {'trip': trip, 'trip_posts': trip_posts, })


@login_required
def trip_edit(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if trip.owner.id != request.user.id:
        raise Http404
    else:    
        if request.method == "POST":
            form = TripForm(request.POST, instance=trip)
            if form.is_valid():
                trip = form.save()
                messages.success(request, 'Trip Saved!')
                return redirect('main:trip_detail', pk=trip.pk)
        else:
            form = TripForm(instance=trip)
    return render(request, 'main/trip_new.html', {'form': form})

@login_required
def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False) 
            trip.owner = request.user
            trip.save()
            messages.success(request, 'Trip successfully created!')
            return redirect('main:trip_detail', pk=trip.pk)
        else:
            messages.error(request, 'Not created yet')     
    else:
        form = TripForm()
    return render(request, 'main/trip_new.html', {'form': form})

@login_required
def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, value=tag_name)
    posts = tag.post_set.filter(trip__owner=request.user).order_by('title')
    return render(request, 'main/tag_detail.html', {'tag': tag, 'posts': posts})

@login_required
def tags_show(request):
    tags = Tag.objects.order_by('value')
    return render(request, 'main/tags_show.html', {'tags': tags})





