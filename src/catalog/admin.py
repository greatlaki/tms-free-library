from django.contrib import admin

from .models import *


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
