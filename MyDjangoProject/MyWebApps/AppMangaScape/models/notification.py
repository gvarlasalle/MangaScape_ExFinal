from django.db import models
from .following import Following
from django.contrib.auth.models import User

class Notification(models.Model):
    NotificationId = models.AutoField(primary_key=True)
    FollowingId = models.ForeignKey(Following, on_delete=models.CASCADE)
    Message = models.CharField(max_length=255)
    ReadNotification = models.BooleanField(default=False)
    NotificationDate = models.DateTimeField(null=True, blank=True)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='notification_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='notification_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification {self.NotificationId} for {self.FollowingId_id}"
