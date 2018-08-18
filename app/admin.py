from django.contrib import admin

from .models import Book, Author, Tag

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'author', 'owner', 'date_added', 'tags_list']

    def tags_list(self, obj):
        return ', '.join([str(t) for t in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']
