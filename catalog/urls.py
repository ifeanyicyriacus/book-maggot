from django.urls import path
from . import views

urlpatterns = [
    # path("", views.get_books),
    # # path('/greet/<name>', views.greet),
    # path('authors/',views.add_author, name="add_author"),
    # path('get/authors/',views.get_authors, name="get_authors"),
    #
    # path('update/authors/<int:pk>/', views.update_author, name="update_author"),
    # path('delete/authors/<int:pk>/', views.delete_author, name="delete_author"),

    path('authors/', views.AddAuthorView.as_view(), name='add_author'),

    path('authors/<int:pk>/', views.GetUpdateDeleteAuthorView.as_view(), name='get_update_and_delete'),



]

