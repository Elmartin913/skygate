from django.shortcuts import render
from django.views import View
from django.http import request
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Book, Author, Tag
from .forms import BookCreateForm


# Create your views here.


class PanelView(View):
    def get(self, request):
        return render(request, 'panel.html')


class BookCreateFormView(View):
    def get(self, request):
        return render(request, 'book_create_form.html')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
