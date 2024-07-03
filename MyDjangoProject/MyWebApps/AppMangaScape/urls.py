from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistListCreate.as_view(), name='artist-list-create'),
    path('authors/', views.AuthorListCreate.as_view(), name='author-list-create'),
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('chapters/', views.ChapterListCreate.as_view(), name='chapter-list-create'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
    path('followings/', views.FollowingListCreate.as_view(), name='following-list-create'),
    path('mangas/', views.MangaListCreate.as_view(), name='manga-list-create'),
    path('manga-categories/', views.MangaCategoryListCreate.as_view(), name='manga-category-list-create'),
    path('notifications/', views.NotificationListCreate.as_view(), name='notification-list-create'),
    path('pages/', views.PageListCreate.as_view(), name='page-list-create'),
    path('permissions/', views.PermissionListCreate.as_view(), name='permission-list-create'),
    path('ratings/', views.RatingListCreate.as_view(), name='rating-list-create'),
    path('readings/', views.ReadingListCreate.as_view(), name='reading-list-create'),
    path('roles/', views.RoleListCreate.as_view(), name='role-list-create'),
    path('role-permissions/', views.RolePermissionListCreate.as_view(), name='role-permission-list-create'),
    path('states/', views.StateListCreate.as_view(), name='state-list-create'),
    path('uploads/', views.UploadListCreate.as_view(), name='upload-list-create'),
    path('mangas/', views.MangaListView.as_view(), name='manga-list'),
    path('mangas/<int:manga_id>/chapters/', views.ChapterListView.as_view(), name='chapter-list'),
    path('chapters/<int:chapter_id>/pages/', views.PageListView.as_view(), name='page-list'),
    path('artists/', views.ArtistListCreate.as_view(), name='artist-list-create'),
    path('authors/', views.AuthorListCreate.as_view(), name='author-list-create'),
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('chapters/', views.ChapterListCreate.as_view(), name='chapter-list-create'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
    path('followings/', views.FollowingListCreate.as_view(), name='following-list-create'),
    path('mangas/', views.MangaListCreate.as_view(), name='manga-list-create'),
    path('manga-categories/', views.MangaCategoryListCreate.as_view(), name='manga-category-list-create'),
    path('notifications/', views.NotificationListCreate.as_view(), name='notification-list-create'),
    path('pages/', views.PageListCreate.as_view(), name='page-list-create'),
    path('permissions/', views.PermissionListCreate.as_view(), name='permission-list-create'),
    path('ratings/', views.RatingListCreate.as_view(), name='rating-list-create'),
    path('readings/', views.ReadingListCreate.as_view(), name='reading-list-create'),
    path('roles/', views.RoleListCreate.as_view(), name='role-list-create'),
    path('role-permissions/', views.RolePermissionListCreate.as_view(), name='role-permission-list-create'),
    path('states/', views.StateListCreate.as_view(), name='state-list-create'),
    path('uploads/', views.UploadListCreate.as_view(), name='upload-list-create'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('chapters/<int:pk>/', views.ChapterDetail.as_view(), name='chapter-detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('followings/<int:pk>/', views.FollowingDetail.as_view(), name='following-detail'),
    path('mangas/<int:pk>/', views.MangaDetail.as_view(), name='manga-detail'),
    path('manga-categories/<int:pk>/', views.MangaCategoryDetail.as_view(), name='manga-category-detail'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='page-detail'),
    path('permissions/<int:pk>/', views.PermissionDetail.as_view(), name='permission-detail'),
    path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='rating-detail'),
    path('readings/<int:pk>/', views.ReadingDetail.as_view(), name='reading-detail'),
    path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),
    path('role-permissions/<int:pk>/', views.RolePermissionDetail.as_view(), name='role-permission-detail'),
    path('states/<int:pk>/', views.StateDetail.as_view(), name='state-detail'),
    path('uploads/<int:pk>/', views.UploadDetail.as_view(), name='upload-detail'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('chapters/<int:pk>/', views.ChapterDetail.as_view(), name='chapter-detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('followings/<int:pk>/', views.FollowingDetail.as_view(), name='following-detail'),
    path('mangas/<int:pk>/', views.MangaDetail.as_view(), name='manga-detail'),
    path('manga-categories/<int:pk>/', views.MangaCategoryDetail.as_view(), name='manga-category-detail'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='page-detail'),
    path('permissions/<int:pk>/', views.PermissionDetail.as_view(), name='permission-detail'),
    path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='rating-detail'),
    path('readings/<int:pk>/', views.ReadingDetail.as_view(), name='reading-detail'),
    path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),
    path('role-permissions/<int:pk>/', views.RolePermissionDetail.as_view(), name='role-permission-detail'),
    path('states/<int:pk>/', views.StateDetail.as_view(), name='state-detail'),
    path('uploads/<int:pk>/', views.UploadDetail.as_view(), name='upload-detail')
]