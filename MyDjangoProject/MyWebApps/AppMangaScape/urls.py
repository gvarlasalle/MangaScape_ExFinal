from django.urls import path
from . import views

urlpatterns = [
    path('mangas/', views.MangaListView.as_view(), name='manga-list'),
    path('mangas/<int:manga_id>/chapters/', views.ChapterListView.as_view(), name='chapter-list'),
    path('chapters/<int:chapter_id>/pages/', views.PageListView.as_view(), name='page-list'),
]