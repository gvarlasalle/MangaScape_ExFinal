from django.db import models
from .role import Role
from .permission import Permission
from django.contrib.auth.models import User

class RolePermission(models.Model):
    RoleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    PermissionId = models.ForeignKey(Permission, on_delete=models.CASCADE)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='role_permission_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='role_permission_modified', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['RoleId', 'PermissionId'], name='unique_role_permission')
        ]
