from django.contrib import admin

# Register your models here.
from    .models.artist          import Artist
from    .models.author          import Author
from    .models.category        import Category
from    .models.chapter         import Chapter
from    .models.comment         import Comment
from    .models.following       import Following
from    .models.manga           import Manga
from    .models.manga_category  import MangaCategory
from    .models.notification    import Notification
from    .models.page            import Page
from    .models.permission      import Permission
from    .models.rating          import Rating
from    .models.reading         import Reading
from    .models.role            import Role
from    .models.role_permission import RolePermission
from    .models.state           import State
from    .models.upload          import Upload


admin.site.register(Artist)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(Comment)
admin.site.register(Following)
admin.site.register(Manga)
admin.site.register(MangaCategory)
admin.site.register(Notification)
admin.site.register(Page)
admin.site.register(Permission)
admin.site.register(Rating)
admin.site.register(Reading)
admin.site.register(Role)
admin.site.register(RolePermission)
admin.site.register(State)
admin.site.register(Upload)