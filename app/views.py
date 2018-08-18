from django.shortcuts import render
from django.views import View
from django.http import request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Book, Author, Tag
from .forms import BookCreateForm


# Create your views here.

# panel
class PanelView(View):
    def get(self, request):
        return render(request, 'panel.html')

# books


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookCreateFormView(View):
    def get(self, request):
        return render(request, 'form.html')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book-list')

# authors


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')

# tags


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'


class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('tag-list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('tag-list')


class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tag-list')
