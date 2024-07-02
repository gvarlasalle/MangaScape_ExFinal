from django.db import models
from .chapter import Chapter
from django.contrib.auth.models import User


class Page(models.Model):
    PageId = models.AutoField(primary_key=True)
    ChapterId = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    PageNumber = models.IntegerField()
    PageImage = models.ImageField(null=True, upload_to="pages")
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='page_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='page_modified', null=True, blank=True, on_delete=models.CASCADE)
    ReadingDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Page {self.PageNumber} of Chapter {self.ChapterId_id} in Manga {self.ChapterId.MangaId_id}"
