from django.contrib import admin

from .models import BookCategory, Book

class BookInLine(admin.TabularInline):
    model = Book
    
class BookCategoryAdmin(admin.ModelAdmin):
    model = BookCategory
    list_display = [
        'name', 
        'description'
    ]
    ordering = ['name']
    inlines = [BookInLine]

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        'title',
        'author',
        'genre',
        'publication_year'
    ]
    ordering = ['-publication_year']


admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)