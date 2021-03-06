from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# from geopy.geocoders import Nominatim
from geopy import geocoders
from geopy.exc import GeocoderQueryError
import pdb



from .models import Post, Trip, Tag
from .forms import PostForm, TagForm, TripForm

User = get_user_model()
g_api_key = 'AIzaSyCbHOjtwPZMpJkxE6EU_YYBfjaB2obZV8w'

def geocode(location_to_geocode):
    # geolocator = Nominatim()
     
    if location_to_geocode is not None:
        try: 
            g = geocoders.GoogleV3(g_api_key)
            # pdb.set_trace()
            location = g.geocode(location_to_geocode)
            coordinates = [location.longitude, location.latitude]
        except (AttributeError, UnboundLocalError, ValueError, GeocoderQueryError): 
            longitude = None
            latitude = None
            coordinates = None   
        return coordinates    
    # if location_to_geocode == None:
    #     pass
    # else:   
    #     location = geolocator.geocode(location_to_geocode) 
    #     coordinates = [location.longitude, location.latitude]
    # #     lon = location.longitude
    # #     lat = location.latitude
    # #     coor_list = (str(lon), str(lat))
    # #     coordinates = (",").join(coor_list)

    #     print("coordinates: ", coordinates)
    #     return coordinates

def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image
    else:
        return '/static/css/main/images/alt_luggage.jpg'        
           

def index(request):
    return render(request, 'main/index.html', {})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_coordinates = [post.lon, post.lat]  
    if post.trip.owner.id != request.user.id:
        raise Http404
    else: 
        post_tags = post.tags.all()

        if post.image:
            popup_content = '<img src="{}" alt="Photo" class="popup-img"/><div class="popup-text"><p>Place: {}</p><p>Trip: <a href="" id="popup-link">{}</a></p></div>'.format(post.image.url, post.place, post.trip.title) 
        else:
            popup_content = '<div class="popup-text"><p>Place: {}</p><p>Trip: <a href="" id="popup-link">{}</a></p></div>'.format(post.place, post.trip.title)             
        marker = {
                "type": "Feature",
                "properties": {
                    "name": post.place,
                    "title": post.title,
                    "text": post.text,
                    "id": post.id,
                    "popupContent": popup_content 
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": post_coordinates
                }
            } 
    context = {
        # 'post_coordinates': post_coordinates,
        'post': post, 
        'post_tags': post_tags, 
        'marker': marker
    }     
    return render(request, 'main/post_detail.html', context)


@login_required
def post_delete(request, pk): 
    post = get_object_or_404(Post, pk=pk)
    if post.trip.owner.id != request.user.id:
        raise Http404
    else:
        post.delete()
        messages.success(request, 'Post deleted!') 
    return redirect('main:trip_detail', slug=post.trip.slug)   


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.trip.owner.id != request.user.id:
        raise Http404
    else: 
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES or None, instance=post, user=request.user)
            if form.is_valid():
                post = form.save(commit=False) 
                coordinates = geocode(post.place)
                if coordinates == None:
                    post.lon = None
                    post.lat = None
                    messages.error(request,'We couldn\'t find a place on the map. Please check a \'country\' name format (Edit option).')
                else:
                    post.lon = coordinates[0]
                    post.lat = coordinates[1]
                post.save()
                form.save_m2m()
                messages.success(request, 'Saved!')
                return redirect('main:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post, user=request.user)
    return render(request, 'main/post_edit.html', {'form': form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, user=request.user)
        if form.is_valid():
            post = form.save(commit=False) 
            coordinates = geocode(post.place)
            if coordinates == None:
                messages.error(request,'We couldn\'t find a place on the map. Please check a \'country\' name format (Edit option).')
            else:
                post.lon = coordinates[0]
                post.lat = coordinates[1]
            post.save()
            form.save_m2m()
            messages.success(request, 'Post successfully created!')
            return redirect('main:post_detail', pk=post.pk)
        else:
            messages.error(request, 'Not created yet')    
    else:
        form = PostForm(user=request.user)
    return render(request, 'main/post_new.html', {'form': form})


@login_required
def tag_new(request):
    tags = Tag.objects.filter(owner=request.user)
    tag_values =[]
    for tag in tags:
        tag_values.append(tag.value)   
    if request.method == "POST":
        form = TagForm(request.POST)
         
        if form.is_valid():
            tag = form.save(commit=False)
            if tag.value in tag_values:
                messages.error(request, 'Tag already exists!')
            else:  
                tag.owner = request.user  
                tag.save()
                messages.success(request, 'Tag successfully created!')
                return redirect('main:tags_show')
        else:
            messages.error(request, 'Not created yet')    
    else:
        form = TagForm()
    return render(request, 'main/tag_new.html', {'form': form})


@login_required
def tag_edit(request, tag_name):
    tags = Tag.objects.filter(owner=request.user)    
    tag = get_object_or_404(tags, value=tag_name)
    if tag.owner.id != request.user.id:
        raise Http404
    else: 
        if request.method == "POST":
            form = TagForm(request.POST, instance=tag)
            if form.is_valid():
                tag = form.save(commit=False)
                tag.owner = request.user
                tag.save()
                messages.success(request, 'Saved!')              
                return redirect('main:tags_show')
        else:
            form = TagForm(instance=tag)
    return render(request, 'main/tag_edit.html', {'form': form})


@login_required
def posts_show(request):
    return render(request, 'main/posts_show.html', {})


@login_required
def trip_delete(request, slug): 
    trip = get_object_or_404(Trip, slug=slug)
    if trip.owner.id != request.user.id:
        raise Http404
    else:
        trip.delete()
        messages.success(request, 'Trip deleted!')
    return redirect('main:trips_show')      


@login_required
def trip_detail(request, slug): 
    trip = get_object_or_404(Trip, slug=slug)
    if trip.owner.id != request.user.id:
        raise Http404
    else:    
        trip_posts = trip.post_set.all().order_by('-created_date')
        
        context = {
        'trip': trip, 
        'trip_posts': trip_posts,
        }      
    return render(request, 'main/trip_detail.html', context)


@login_required
def trip_edit(request, slug):
    trip = get_object_or_404(Trip, slug=slug)
    if trip.owner.id != request.user.id:
        raise Http404
    else:    
        if request.method == "POST":
            form = TripForm(request.POST, request.FILES, instance=trip)
            if form.is_valid():
                trip = form.save(commit=False) 
                trip.image = image_url(trip)
                coordinates = geocode(trip.country)
                if coordinates == None:
                    trip.lon=None
                    trip.lat=None
                    messages.error(request,'We couldn\'t find a place on the map. Please check a \'country\' name format (Edit option).')
                else:
                    trip.lon = coordinates[0]
                    trip.lat = coordinates[1]
                trip.save()                
                messages.success(request, 'Trip Saved!')
                return redirect('main:trip_detail', slug=trip.slug)
        else:
            form = TripForm(instance=trip)
    return render(request, 'main/trip_edit.html', {'form': form})


@login_required
def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES or None) 
        if form.is_valid():
            trip = form.save(commit=False) 
            trip.owner = request.user
            trip.image = image_url(trip)
            coordinates = geocode(trip.country)
            if coordinates == None:
                messages.error(request,'We couldn\'t find a place on the map. Please check a \'country\' name format (Edit option).')
            else:
                trip.lon = coordinates[0]
                trip.lat = coordinates[1]
            trip.save()
            print("lon,lat: ", trip.lon, trip.lat)
            messages.success(request, 'Trip successfully created!')
            return redirect('main:trip_detail', slug=trip.slug)
        else:
            messages.error(request, 'Not created yet')     
    else:
        form = TripForm()
    return render(request, 'main/trip_new.html', {'form': form})


@login_required
def trips_show(request):
    list_of_trips = Trip.objects.filter(owner=request.user).order_by('title')
    
    paginator = Paginator(list_of_trips, 9) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        list_of_trips = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        list_of_trips = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        list_of_trips = paginator.page(paginator.num_pages)

    context = {
        'list_of_trips': list_of_trips
        }
    return render(request, 'main/trips_show.html', context)


@login_required
def tag_delete(request, tag_name): 
    tag = get_object_or_404(Tag, value=tag_name)
    if tag.owner.id != request.user.id:
        raise Http404
    else:
        tag.delete()
        messages.success(request, 'Post deleted!') 
    return redirect('main:tags_show')   

@login_required
def tag_detail(request, tag_name):
    tags = Tag.objects.filter(owner=request.user)
    tag = get_object_or_404(tags, value=tag_name)
    if tag.owner.id != request.user.id:
        raise Http404
    else: 
        posts = tag.post_set.filter(trip__owner=request.user).order_by('title')
    return render(request, 'main/tag_detail.html', {'tag': tag, 'posts': posts})


@login_required
def tags_show(request):
    tags = Tag.objects.filter(owner=request.user).order_by('value')
    return render(request, 'main/tags_show.html', {'tags': tags})


@login_required
def photos_show(request):
    trips = Trip.objects.filter(owner=request.user).order_by('title')
    posts = Post.objects.filter(trip__owner=request.user)    
    context = {
        'trips': trips,
        'posts': posts,
    } 
    return render(request, 'main/photos_show.html', context) 


@login_required
def map(request):
    trips = Trip.objects.filter(owner=request.user)

    markers = []

    for trip in trips:
        if trip.image:
            popup_content = '<img src="{}" alt="Photo" class="popup-img"/><div class="popup-text"><p>Country: {}</p><p>Trip: {}</p></div>'.format(trip.image.url, trip.country, trip.title) 
        else:
            popup_content = '<div class="popup-text"><p>Country: {}</p><p>Trip: {}</p></div>'.format(trip.country, trip.title)  #not used           
        

        if not trip.lon:
            continue
        coordinates = [trip.lon, trip.lat]   
        marker = {
                "type": "Feature",
                "properties": {
                    "name": trip.country,
                    "title": trip.title,
                    "id": trip.id,
                    "popupContent": popup_content 
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates
                }
            }    
        markers.append(marker)      
    
    context = {
        'markers': markers
    } 

    return render(request, 'main/map.html', context) 


