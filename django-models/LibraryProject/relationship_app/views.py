from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.decorators import login_required

# @login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# User Login View

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'relationship_app/login.html', {'form': form})
    
#User Logout View
class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    # context_object_name = "logout"


# def user_logout(request):
#     logout(request)
#     return render(request, 'relationship_app/logout.html')


#User Registration

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
    