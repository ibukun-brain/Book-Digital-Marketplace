from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView, ListView, View
)
from books.models import ( 
    Book, Chapter, Exercise, Solution
)
from shopping_cart.models import Order, OrderItem
from digital_marketplace.utils.helpers import check_book_relationship

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 25
    template_name = 'books/book_list.html'

    
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        request = self.request
        book_status = check_book_relationship(request, book)
        context.update({
            'book_status':book_status
        }) 
        return context

class BookChapterDetailView(DetailView):
    model = Chapter
    context_object_name = 'chapter'    
    template_name = 'books/book_chapter_detail.html'
    query_pk_and_slug = True
    slug_field = 'book__slug'
    slug_url_kwarg = 'book_slug'
    pk_url_kwarg = 'chapter_number'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = self.object
        request = self.request
        book_status = check_book_relationship(request, chapter.book)
        context.update({
            'book_status':book_status
        }) 
        return context


class BookExerciseDetailView(View):

    def get(self, request, book_slug, chapter_number, exercise_number):
        exercise = get_object_or_404(
            Exercise, 
            chapter__book__slug=book_slug,
            chapter__chapter_number=chapter_number,
            exercise_number=exercise_number,
        )
        request = self.request
        book_status = check_book_relationship(request, exercise.chapter.book)
        context = {
            "exercise": exercise,
            'book_status':book_status
        }
        return render(request, 'books/book_exercise_detail.html', context)



