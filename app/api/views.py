from rest_framework import generics
from app.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer
    #queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.all()

    # def get_object(self)
    #    pk = self.kwars.get('pk')
    #    return Book.objects.get(pk=pk)
