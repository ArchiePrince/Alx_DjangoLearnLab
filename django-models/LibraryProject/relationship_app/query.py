# import os
# import django

# # Set up Django environment
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
# django.setup()

# from relationship_app.models import Author, Book, Library, Librarian

# # Query all books by a specific author
# def books_by_author(author_name):
#     author = Author.objects.filter(name=author_name).first()
#     if author:
#         books = Book.objects.filter(author=author)
#         return [book.title for book in books]
#     return []

# # List all books in a library
# def books_in_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         return [book.title for book in library.books.all()]
#     return []

# # Retrieve the librarian for a library
# def librarian_of_library(library_name):
#     library = Library.objects.filter(name=library_name).first()
#     if library:
#         librarian = Librarian.objects.filter(library=library).first()
#         return librarian.name if librarian else None
#     return None

# # Sample test cases
# if __name__ == "__main__":
#     print("Books by 'J.K. Rowling':", books_by_author("J.K. Rowling"))
#     print("Books in 'Central Library':", books_in_library("Central Library"))
#     print("Librarian of 'Central Library':", librarian_of_library("Central Library"))