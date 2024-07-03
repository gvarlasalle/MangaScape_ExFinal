from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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
from .serializer import ArtistSerializer, AuthorSerializer, CategorySerializer, ChapterSerializer, CommentSerializer, FollowingSerializer, MangaSerializer, MangaCategorySerializer, NotificationSerializer, PageSerializer, PermissionSerializer, RatingSerializer, ReadingSerializer, RoleSerializer, RolePermissionSerializer, StateSerializer, UploadSerializer

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ChapterListCreate(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FollowingListCreate(generics.ListCreateAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

class MangaListCreate(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class MangaCategoryListCreate(generics.ListCreateAPIView):
    queryset = MangaCategory.objects.all()
    serializer_class = MangaCategorySerializer

class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class PageListCreate(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PermissionListCreate(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class RatingListCreate(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReadingListCreate(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class RoleListCreate(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RolePermissionListCreate(generics.ListCreateAPIView):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class StateListCreate(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class UploadListCreate(generics.ListCreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

class MangaListView(generics.ListAPIView):
    serializer_class = MangaSerializer

    def get_queryset(self):
        user = self.request.user
        return Manga.objects.filter(CreatedByUserId=user)
    
class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class ChapterListView(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        manga_id = self.kwargs['manga_id']
        return Chapter.objects.filter(MangaId=manga_id)

class PageListView(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Page.objects.filter(ChapterId=chapter_id)
    
class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FollowingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class MangaCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MangaCategory.objects.all()
    serializer_class = MangaCategorySerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RolePermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class UploadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer