from rest_framework import serializers
from app.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'pk',
            'title',
            'author',
            'gender',
            'isbn',
            'tags',
            'date_added'
        ]
