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
            'date_added',
        ]
        read_only_fields = ['pk']

    def validate_title(self, value):
        qs = Book.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return value
