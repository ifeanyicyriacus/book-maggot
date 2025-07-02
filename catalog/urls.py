from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_books),
    # path('/greet/<name>', views.greet),
    path('authors',views.get_authors),
]

