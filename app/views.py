from django.shortcuts import render
from django.views import View
from django.http import request, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


from .models import Book, Author, Tag
from .forms import BookCreatorStep1Form, BookCreatorStep2Form


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


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book-list')


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')

# book creator


class BookCreatorStep1View(View):
    def get(self, request):
        form = BookCreatorStep1Form()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookCreatorStep1Form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            gender = form.cleaned_data['gender']
            isbn = form.cleaned_data['isbn']
            new_book = Book.objects.create(
                title=title,
                gender=gender,
                isbn=isbn,
            )

        url = reverse('book-creator2', kwargs={'book_id': new_book.id})
        return HttpResponseRedirect(url)


class BookCreatorStep2View(View):
    def get(self, request, book_id):
        form = BookCreatorStep2Form()
        return render(request, 'form.html', {'form': form})


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
