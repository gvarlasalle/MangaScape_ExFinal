from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    ArtistId = models.AutoField(primary_key=True)
    ArtistName = models.CharField(max_length=100)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='artist_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='artist_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ArtistName
