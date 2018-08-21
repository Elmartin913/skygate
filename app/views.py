from django.shortcuts import render, redirect
from django.views import View
from django.http import request, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


from .models import Book, Author, Tag
from .forms import SignUpForm


# Create your views here.

class StartView(View):
    def get(self, requset):
        return TemplateResponse(requset, 'index.html')

# panel


class PanelView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'panel.html')

# books


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book-list')


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


# authors


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


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


# account
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('panel')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
