from .models import Book, Author, Tag


def lists(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'books': books,
        'authors': authors,
        'tags': tags
    }
    return ctx
