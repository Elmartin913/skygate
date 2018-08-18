from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GENRES = (
    (1, 'horror'),
    (2, 'sci-fi'),
    (3, 'comedy'),
)


class Book(models.Model):
    title = models.CharField(max_length=256)
    gender = models.IntegerField(choices=GENRES)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='books')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(null=True, max_length=256)
    # books

    def __str__(self):
        return self.tag_name
