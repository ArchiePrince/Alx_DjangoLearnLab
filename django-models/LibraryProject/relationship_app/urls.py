from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView
from .views import register

urlpatterns = [
    path("books/", list_books, name="home"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path('login/', UserLoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path("logout/", UserLogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register")
]
