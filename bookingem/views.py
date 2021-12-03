from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, \
    DetailView, DeleteView, CreateView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic.edit import FormMixin
from . import models, forms
from bookingem.models import Comment
from bookingem.forms import CommentForm



class BookListView(ListView):
    template_name = "book/book_list.html"
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return models.Books.objects.all()

class BookCreateView(CreateView):
    template_name = "book/book_create.html"
    form_class = forms.BookForm
    success_url = "/"
    queryset = models.Books.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)

class BookDetailView(DetailView):
    template_name = "book/book_detail.html"
    model = models.Books
    form_class = forms.CommentForm


    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)
    #
    # def form_valid(self, form):
    #     form.instance.post_id = self.kwargs["id"]
    #     return super().form_valid(form=form)

    def get_context_data(self, **kwargs):
        context: dict = super(BookDetailView, self).get_context_data(**kwargs)
        id = self.kwargs.get("id")
        comments: list[Comment] = Comment.objects.filter(comment_id=id)
        context["comments"] = comments
        return context


def create_comment_view(request: HttpRequest, id):
    if request.method == "POST":
        data = request.POST
        if data.get("text"):
            Comment.objects.create(text=data["text"], comment_id=id)
            return redirect("/")
        else:
            return HttpResponse("Empty field!!!")
# class CommentCreate(CreateView):
#     model = Comment
#     template_name = "book/book_detail.html"
#     extra_context = {"comment": forms.CommentForm}
#
#     def get_context_data(self, **kwargs):   # передача формы
#         context = super(CommentCreate, self).get_context_data(**kwargs)
#         context["comment"] = CommentForm()
#         return context
#
#     def get_success_url(self):
#         return redirect, reverse_lazy("book-detail", kwargs={"pk": self.get_object().id})

class BookUpdateView(UpdateView):
    template_name = "book/book_create.html"
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("book:book-list")


class BookDeleteView(DeleteView):
    template_name = "book/book_delete.html"

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def get_success_url(self):
        return reverse("book:book-list")

