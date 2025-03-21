# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'LibraryProject.settings')
# django.setup()

from relationship_app.models import Author, Book, Librarian, Library

#Query samples from the Relationship App

#Creating objects for the models

author_name = Author(name='Efo Mawugbe')
author_name.save()

author2 = Author.objects.create(name='George Orwell')
author3 = Author.objects.create(name='J.K. Rowling')



"""
OR in one-step:
author = Author.objects.create(name='Efo Mawugbe')

"""

#Creating object for the ForeignKey table, Book

new_book1 = Book.objects.create(title='In the chest of a woman', author=author_name)

# chest_book = Book.objects.get(pk=1)
# auth_book = Author.objects.get(id=1)
# new_book1.author = auth_book
# new_book1.save()


new_book2 = Book.objects.create(title='1984', author=author2)

# ge_book = Book.objects.get(pk=2)
# auth_book2 = Author.objects.get(id=2)
# new_book2.author = auth_book2
# new_book2.save()

new_book3 = Book.objects.create(title='Animal Farm', author=author3)
# auth_book3 = Author.objects.get(id=2)
# new_book3.author = auth_book3
# new_book3.save()


#Creating objects for ManyToMany table, Library

library_name = Library.objects.create(name='Central City Library')
library2 = Library.objects.create(name='British National Library')
library3 = Library.objects.create(name='National Library of Ghana')

library_name.book.add(new_book1, new_book2, new_book3)
library2.book.add(new_book2, new_book3)
library3.book.add(new_book1, new_book3)



#Creating objects for OneToOne table, Librarian

librarian1 = Librarian.objects.create(name='John Smith', library=library_name)
librarian2 = Librarian.objects.create(name='Sarah Johnson', library=library2)
librarian3 = Librarian.objects.create(name='Aisha Mensah', library=library3)


#Query all books by a specific author

# --> Book.objects.filter(author__id=2)
objects = Author.objects.get(name=author_name)
objects.filter(author=author)


#List all books in a library
books = Library.objects.get(name=library_name)
books.all()

#Retrieve Librarian for a library
Librarian.objects.get(library=library_name)