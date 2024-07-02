from django.db import models
from django.contrib.auth.models import User

class Permission(models.Model):
    PermissionId = models.AutoField(primary_key=True)
    PermissionName = models.CharField(max_length=50)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='permission_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='permission_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.PermissionName
