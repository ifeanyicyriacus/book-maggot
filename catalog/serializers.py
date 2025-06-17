from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary', 'author']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # summary= serializers.CharField(max_length=255)
