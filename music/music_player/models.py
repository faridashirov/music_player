from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT, related_name='songs')
    mp3_file = models.FileField(
        upload_to='songs/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    cover_image = models.ImageField(upload_to='media/covers/', null=True, blank=True)

    def get_cover(self):
        if self.cover_image:
            return self.cover_image.url
        return self.artist.photo.url

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='media/artists/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name