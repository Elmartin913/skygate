from django.db import models
from django.conf import settings


# Create your models here.

GENRES = (
    (1, 'horror'),
    (2, 'sci-fi'),
    (3, 'comedy'),
)


class Book(models.Model):
    title = models.CharField(max_length=256)
    gender = models.IntegerField(choices=GENRES, blank=True)
    isbn = models.CharField(max_length=17)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='books', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def owner(self):
        return self._user


class Author(models.Model):
    author_name = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.author_name


class Tag(models.Model):
    tag_name = models.CharField(null=True, max_length=256, blank=True)
    # books

    def __str__(self):
        return self.tag_name
