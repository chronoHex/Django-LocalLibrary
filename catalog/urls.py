"""
url pattern file for catalog app
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Book paths
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # Author paths
    path('authors/', views.AuthorListView.as_view(), name = 'authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # Loaned books for reg'd users path
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # All loaned books just for librarian users 
    path('borrowed/', views.AllLoanedBooks.as_view(), name='all-borrowed'),
    # Path for form renewal (notice the difference between class-created views and function views :)
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    # Paths for the author create, edit, delete views
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),

    # Paths for book create, edit, and delete views
    path('book/create/', views.BookCreate.as_view(), name="book_create"),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='author_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='author_delete'),
]
