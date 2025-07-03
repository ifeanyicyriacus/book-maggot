# from rest_framework import serializers
#
# from catalog.models import Author
# from
#
# #
# # class BookSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model=Book
# #         fields = ['id', 'title', 'summary']
#
# class AuthorSerializer(serializers.ModelSerializer):
#     # book = BookSerializer(many=True, read_only=True)
#     class Meta:
#         model=Author
#         fields = ['first_name', 'last_name', 'email', 'dob']
#
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']