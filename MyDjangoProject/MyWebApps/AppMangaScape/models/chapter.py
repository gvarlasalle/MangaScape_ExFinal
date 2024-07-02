from django.db import models
from .manga import Manga
from django.contrib.auth.models import User

class Chapter(models.Model):
    ChapterId = models.AutoField(primary_key=True)
    MangaId = models.ForeignKey(Manga, on_delete=models.CASCADE)
    ChapterNumber = models.IntegerField()
    Title = models.CharField(max_length=255, blank=True)
    PublicationDate = models.DateField(null=True, blank=True)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='chapter_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='chapter_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Chapter {self.ChapterNumber} of {self.MangaId.Title}"
