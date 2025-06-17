from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Author, User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

# Register your models here.
# admin.site.register(User)
@admin.register(Author)
class AuthorAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "email", "password1", "password2", "phone", "dob",
                           "dod"),
                # "fields": ("username", "first_name", "last_name", "email", "usable_password", "password1", "password2", "phone"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'phone', 'dob', 'dod']
    list_display_links =['email', 'dob', 'dod']
    list_editable = ['first_name', 'last_name', 'phone']
# admin.site.register(Author)
