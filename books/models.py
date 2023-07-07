import auto_prefetch
from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from digital_marketplace.utils.models import (
    NamedTimeBasedModel, TimeBasedModel
)
from digital_marketplace.utils.media import (
    book_image_upload_path, solution_image_upload_path
)

# Create your models here.

class UserLibrary(TimeBasedModel):
    user = auto_prefetch.OneToOneField(
        "home.CustomUser",
        on_delete=models.CASCADE,
    )
    books = models.ManyToManyField('Book', blank=True)

    def book_list(self):
        return self.books.all()

    class Meta(auto_prefetch.Model.Meta):
        verbose_name = "User Library"
        verbose_name_plural = "User Library"

    def __str__(self):
        return f"{self.user} - Library"
    
    
class Author(NamedTimeBasedModel):
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    

class Book(NamedTimeBasedModel):
    author = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=216)
    cover_image = models.ImageField(
        # default="",
        upload_to=book_image_upload_path,
        blank=True,
    )
    slug = models.SlugField(unique=True, blank=True)
    price = models.FloatField()

    def cover_image_url(self):
        if self.cover_image:
            return self.cover_image.url
            
        return f"{settings.MEDIA_URL}/default/book.png"

    def get_absolute_url(self):
        return   reverse("books:book-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name


class Chapter(NamedTimeBasedModel):
    book = auto_prefetch.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE
    )
    chapter_number = models.PositiveSmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse("books:chapter-detail", 
            kwargs={
                "book_slug": self.book.slug,
                "chapter_number": self.chapter_number
            }
        )
    

    def __str__(self):
        return self.name
    
class Exercise(NamedTimeBasedModel):
    chapter = auto_prefetch.ForeignKey(
        'books.Chapter',
        on_delete=models.CASCADE
    )
    exercise_number = models.PositiveSmallIntegerField(default=0)
    page_number = models.PositiveSmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse("books:exercise-detail", 
            kwargs={
                "book_slug": self.chapter.book.slug,
                "chapter_number": self.chapter.chapter_number,
                "exercise_number": self.exercise_number
            }
        )

    def __str__(self):
        return self.name


class Solution(models.Model):
    exercise = auto_prefetch.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )
    solution_number = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(
        upload_to=solution_image_upload_path
    )

    def __str__(self):
        return f"Solution to {self.exercise.name}"
    
    def image_url(self):
        if self.image:
            return self.image.url
            
        return f"{settings.MEDIA_URL}/default/book.png"
    

    def image_url(self):
        if self.image_url:
            return self.image.url
            
        return f"{settings.MEDIA_URL}/default/book.png"