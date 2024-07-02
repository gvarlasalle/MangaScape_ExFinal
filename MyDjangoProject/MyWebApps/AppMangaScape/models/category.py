from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='category_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='category_modified', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.CategoryName
