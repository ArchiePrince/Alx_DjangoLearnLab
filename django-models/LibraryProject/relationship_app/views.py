from django.views.generic import DetailView
from .models  import Library, Book
from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library/library_detail.html"
    context_object_name = "library"