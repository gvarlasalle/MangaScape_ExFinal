from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=50)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='role_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='role_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.RoleName
