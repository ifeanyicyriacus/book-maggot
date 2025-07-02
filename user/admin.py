from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from catalog.models import Author

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "email", "password1", "password2", "phone"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'phone']
    list_display_links = ['email']
    list_editable = ['first_name', 'last_name', 'phone']
    list_per_page = 10

# Register your models here.
# admin.site.register(User)
# @admin.register(Author)
# class AuthorAdmin(BaseUserAdmin):
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "first_name", "last_name", "email", "password1", "password2", "phone", "dob",
    #                        "dod"),
    #             # "fields": ("username", "first_name", "last_name", "email", "usable_password", "password1", "password2", "phone"),
    #         },
    #     ),
    # )
    # list_display = ['first_name', 'last_name', 'email', 'phone', 'dob', 'dod']
    # list_display_links =['email', 'dob', 'dod']
    # list_editable = ['first_name', 'last_name', 'phone']
    # list_per_page = 10

# admin.site.register(Author)
