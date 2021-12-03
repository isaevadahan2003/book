from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path("", views.BookListView.as_view(), name= "book-list"),
    path("create/", views.BookCreateView.as_view(), name= "book-create"),
    path("<int:id>/delete/", views.BookDeleteView.as_view(), name="book-delete"),
    path("<int:id>/", views.BookDetailView.as_view(), name= "book-detail"),
    path("<int:id>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path("<int:id>/comment/", views.create_comment_view, name="book-comment"),

]