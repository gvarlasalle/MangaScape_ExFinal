from django.db import models
from .chapter import Chapter
from django.contrib.auth.models import User

class Reading(models.Model):
    ReadingId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    ChapterId = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    PageNumber = models.IntegerField()
    Status = models.CharField(max_length=20, choices=[('in progress', 'in progress'), ('completed', 'completed')], default='in progress')
    ReadingDate = models.DateField()
    ReadingTime = models.TimeField()
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='reading_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='reading_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reading {self.ReadingId} by {self.UserId_id} on Chapter {self.ChapterId_id}"
