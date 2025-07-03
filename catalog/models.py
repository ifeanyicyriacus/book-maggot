import uuid

from django.conf import settings
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=False, null=False)
    dod = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

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
        ("C", "COMEDY"),
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

class BookImage(models.Model):
    image = models.ImageField(upload_to="book/images/", null=True, blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.name