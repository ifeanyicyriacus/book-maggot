import uuid

# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from user.models import Author


# class Author(settings.AUTH_USER_MODEL):
#     dob = models.DateField(blank=False, null=False)
#     dod = models.DateField(blank=True, null=True)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name='books')
    summary = models.TextField()
    isbn = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A", "AVAILABLE"),
        ("B", "BORROWED"),
        ("M", "MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A")
    return_date = models.DateTimeField(blank=False, null = False)
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class Genre(models.Model):
    GENRE_CHOICES = (
        ("D", "DRAMA"),
        ("R", "ROMANCE"),
        ("D", "COMEDY"),
        ("F", "FINANCE"),
        ("P", "POLITICS"),
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="DRAMA", unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("EN", "ENGLISH"),
        ("FR", "FRENCH"),
        ("FI", "FINNISH"),
    )
    name = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="ENGLISH")

    def __str__(self):
        return self.name