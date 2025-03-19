

from .models import Book
from django.shortcuts import render

from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    from .models  import Library
    
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"