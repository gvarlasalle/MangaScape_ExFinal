from django.db import models
from .manga import Manga
from django.contrib.auth.models import User

class Following(models.Model):
    FollowingId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    MangaId = models.ForeignKey(Manga, on_delete=models.CASCADE)
    FollowingDate = models.DateField()
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='following_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='following_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Following {self.FollowingId} by {self.UserId_id} on Manga {self.MangaId_id}"
