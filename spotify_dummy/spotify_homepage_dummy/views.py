from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Playlist
from django.contrib.auth.decorators import login_required

# Create your views here.
def some_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('user_auth:login_register_view'))

#@login_required
def home(request):
    playlist = Playlist.objects.all()
    return render(request, "homepage.html", {'playlist': playlist})

#@login_required
def songs(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.songs_set.all()
    return render(request, 'songs.html', {'playlist': playlist, 'songs': songs})
