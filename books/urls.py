from django.urls import path
from books import views as books_views

app_name = 'books'

urlpatterns = [
    path(
        route='',
        view=books_views.BookListView.as_view(),
        name='book-list' 
    ),
    path(
        route='book/<slug:slug>/',
        view=books_views.BookDetailView.as_view(),
        name='book-detail' 
    ),
    path(
        route='book/<slug:book_slug>/<int:chapter_number>/',
        view=books_views.BookChapterDetailView.as_view(),
        name='chapter-detail', 
    ),
     path(
        route='book/<slug:book_slug>/<int:chapter_number>/<int:exercise_number>',
        view=books_views.BookExerciseDetailView.as_view(),
        name='exercise-detail', 
    ),
]
