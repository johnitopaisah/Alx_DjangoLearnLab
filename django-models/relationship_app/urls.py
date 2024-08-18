from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, CustomLogoutView, RegisterView


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', login_view, name='login'),  # Function-based view for login
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Class-based view for logout
    path('register/', RegisterView.as_view(), name='register'),  # Class-based view for registration
]
