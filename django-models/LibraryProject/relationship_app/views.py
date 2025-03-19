from django.shortcuts import render
from .models  import Book, Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationships/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library/library_detail.html"
    context_object_name = "library"