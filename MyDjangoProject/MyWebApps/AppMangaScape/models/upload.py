from django.db import models
from .manga import Manga
from django.contrib.auth.models import User

class Upload(models.Model):
    UploadId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    MangaId = models.ForeignKey(Manga, on_delete=models.CASCADE)
    UploadDate = models.DateTimeField(null=True, blank=True)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='upload_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='upload_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Upload {self.UploadId} by {self.UserId_id} of Manga {self.MangaId_id}"
