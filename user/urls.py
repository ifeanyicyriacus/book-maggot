from django.urls import path
from . import views

urlpatterns = [
    path("authors", views.get_authors),
]
