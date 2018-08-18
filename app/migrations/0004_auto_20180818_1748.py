# Generated by Django 2.1 on 2018-08-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='book',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'horror'), (2, 'sci-fi'), (3, 'comedy')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='books', to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]