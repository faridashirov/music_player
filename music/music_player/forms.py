from .models import Song, Artist
from django import forms

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'mp3_file', 'cover_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'artist': forms.Select(attrs={'class': 'form-input'}),  # добавили класс
            'mp3_file': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
    
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'bio': forms.Textarea(attrs={'class': 'form-input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }