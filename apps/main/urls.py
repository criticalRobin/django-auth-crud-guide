from django.urls import path
from .views.authors.views import (
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
)
from .views.publishers.views import (
    PublisherListView,
    PublisherCreateView,
    PublisherUpdateView,
    PublisherDeleteView,
)
from .views.books.views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

app_name = "main"

urlpatterns = [
    # AUTHOR URLS
    path("author/list/", AuthorListView.as_view(), name="author_list"),
    path("author/create/", AuthorCreateView.as_view(), name="author_create"),
    path("author/update/<int:pk>/", AuthorUpdateView.as_view(), name="author_update"),
    path("author/delete/<int:pk>/", AuthorDeleteView.as_view(), name="author_delete"),
    #   PUBLISHER URLS
    path("publisher/list/", PublisherListView.as_view(), name="publisher_list"),
    path("publisher/create/", PublisherCreateView.as_view(), name="publisher_create"),
    path(
        "publisher/update/<int:pk>/",
        PublisherUpdateView.as_view(),
        name="publisher_update",
    ),
    path(
        "publisher/delete/<int:pk>/",
        PublisherDeleteView.as_view(),
        name="publisher_delete",
    ),
    #  BOOK URLS
    path("book/list/", BookListView.as_view(), name="book_list"),
    path("book/create/", BookCreateView.as_view(), name="book_create"),
    path("book/update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("book/delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
]
