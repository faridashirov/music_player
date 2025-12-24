from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Artist
from .forms import SongForm, ArtistForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})

def artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})

def artist_detail(request, slug):
    artist = Artist.objects.get(slug=slug)
    songs = artist.songs.all()
    return render(request, 'artist_detail.html', {'artist': artist, 'songs': songs})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Неверное имя пользователя или пароль"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def signupview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': "Пользователь уже существует"})

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Пароли не совпадают"
            return render(request, 'signup.html', {'error_message': error_message})
    return render(request, 'signup.html')


def logoutview(request):
    logout(request)
    return redirect('home')

def delete_artist(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    artist.delete()
    return redirect('artists')