from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AuthorSerializer
from .models import Author


# Create your views here.
@api_view()
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


