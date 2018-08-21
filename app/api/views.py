from django.db.models import Q
from rest_framework import generics, mixins

from app.models import Book
from .serializers import BookSerializer
from .permission import IsOwnerOrReadOnly


class BookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = Book.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)
            ).distinct()
        return qs

    def post(self, serializer):
        return self.create(self.request)


class BookRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Book.objects.get(pk=pk)
