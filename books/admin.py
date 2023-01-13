from django.contrib import admin
from books.models import (
    Author, Book, Chapter, 
    Exercise, Solution, UserLibrary
)

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    filter_horizontal = ['author']
    search_fields = ['author__name', 'name']
    list_filter = ['created_at']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['book', 'chapter_number', 'name', 'created_at']
    ordering = ['chapter_number']
    list_filter = ['created_at']
    search_fields = ['book__name', 'name']
    list_select_related = ['book']
    autocomplete_fields = ['book']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'name', 'exercise_number', 'page_number']
    ordering = ['exercise_number','chapter__number']
    search_fields = ['chapter__name', 'name']
    list_select_related = ['chapter']
    autocomplete_fields = ['chapter']


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_select_related = ['exercise']
    autocomplete_fields = ['exercise']
    search_fields = ['exercise__name']
    ordering = ['exercise__exercise_number']


@admin.register(UserLibrary)
class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_select_related = ['user']
    autocomplete_fields = ['user']
    filter_horizontal = ['books']
    search_fields = ['user__username', 'books__name']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = "created_at"
