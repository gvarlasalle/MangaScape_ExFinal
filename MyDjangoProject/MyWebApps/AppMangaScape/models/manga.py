from django.db import models
from .state import State
from .author import Author
from .artist import Artist
from django.contrib.auth.models import User

class Manga(models.Model):
    MangaId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Authors = models.ManyToManyField(Author, related_name='mangas', blank=True)
    Artists = models.ManyToManyField(Artist, related_name='mangas', blank=True)
    PublicationDate = models.DateField(null=True, blank=True)
    StateId = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='manga_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='manga_modified', null=True, blank=True, on_delete=models.CASCADE)
    MangaCreationDate = models.DateField(null=True, blank=True)
    IsFree = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
