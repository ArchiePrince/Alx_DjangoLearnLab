# Detailed CRUD Operations in the Django Shell
### Delete:
> from bookshelf.models import Book

>>> new_book.delete()
<!-- (1, {'bookshelf.Book': 1})-->
>>> Book.objects.all()
<!-- <QuerySet []>-->