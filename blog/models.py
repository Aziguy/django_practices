from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Fill the category name.")
    slug = models.SlugField(blank=True, help_text="This field will be automatically fill.")


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, help_text="Title of your article.")
    slug = models.SlugField(blank=True, help_text="This field will be automatically fill.")
    published = models.BooleanField(default=False, help_text="Set if article has to be published or not.")
    date = models.DateField(blank=True, null=True, help_text="Set this field the day when you published our article.")
    content = models.TextField(help_text="Fill the content of our article.")
    description = models.TextField(default='', help_text='Fill the description of article.')

    @property
    def published_string(self):
        if self.published:
            return "L'article est publiée"
        return "L'article est est inaccessible"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Book(models.Model):
    CAT = (
        ('Aventure', 'Aventure'),
        ('Thriller', 'Thriller'),
        ('Fantastique', 'Fantastique'),
        ('Romance', 'Romance'),
        ('Horreur', 'Horreur'),
        ('Science-fiction', 'Science-fiction')
    )

    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=25, choices=CAT, default='NULL', blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
