from rest_framework import serializers

from catalog.models import Book
from .models import Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ['id', 'title', 'summary']

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    class Meta:
        model=Author
        fields = ['first_name', 'last_name', 'email', 'book']
