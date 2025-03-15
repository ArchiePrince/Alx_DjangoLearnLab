# Detailed CRUD Operations in the Django Shell
### Create:
> from bookshelf.models import Book
new_book = Book(title='1984', author = 'George Orwell', publication_year = 1949)
> new_book
<!-- <Book: 1984> -->

### Retrieve:
> from bookshelf.models import Book

Book.objects.all()
<!-- <QuerySet [<Book: 1984>]>-->

### Update:
> from bookshelf.models import Book

>>> new_book.title = 'Nineteen Eighty-Four'
>>> new_book.save()
>>> new_book
<!-- <Book: Nineteen Eighty-Four>-->

### Delete:
> from bookshelf.models import Book

>>> new_book.delete()
<!-- (1, {'bookshelf.Book': 1})-->
>>> Book.objects.all()
<!-- <QuerySet []>-->