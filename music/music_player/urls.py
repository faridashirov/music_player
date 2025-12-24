from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists, name='artists'),
    path('add-song/', views.add_song, name='add_song'),
    path('add-artist/', views.add_artist, name='add_artist'),
    path('artist/<slug:slug>/', views.artist_detail, name='artist_detail'),
    path('signup', views.signupview, name='signup'),
    path('login', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('delete-artist/<slug:slug>/', views.delete_artist, name='delete_artist'),
]
