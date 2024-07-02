from rest_framework import serializers
from .models.artist import Artist
from .models.author import Author
from .models.category import Category
from .models.chapter import Chapter
from .models.comment import Comment
from .models.following import Following
from .models.manga import Manga
from .models.manga_category import MangaCategory
from .models.notification import Notification
from .models.page import Page
from .models.permission import Permission
from .models.rating import Rating
from .models.reading import Reading
from .models.role import Role
from .models.role_permission import RolePermission
from .models.state import State
from .models.upload import Upload

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['ArtistId', 'ArtistName']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['AuthorId', 'AuthorName']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    Authors = AuthorSerializer(many=True)
    Artists = ArtistSerializer(many=True)

    class Meta:
        model = Manga
        fields = ['MangaId', 'Title', 'Description', 'Authors', 'Artists']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Authors'] = AuthorSerializer(instance.Authors.all(), many=True).data
        representation['Artists'] = ArtistSerializer(instance.Artists.all(), many=True).data
        return representation

class MangaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaCategory
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'