from django.db import models
from .manga import Manga
from .category import Category
from django.contrib.auth.models import User

class MangaCategory(models.Model):
    MangaId = models.ForeignKey(Manga, on_delete=models.CASCADE)
    CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    RecordCreationDate = models.DateTimeField(auto_now_add=True)
    RecordModificationDate = models.DateTimeField(null=True, blank=True)
    CreatedByUserId = models.ForeignKey(User, related_name='manga_category_created', on_delete=models.CASCADE)
    ModifiedByUserId = models.ForeignKey(User, related_name='manga_category_modified', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MangaId', 'CategoryId'], name='unique_manga_category')
        ]
