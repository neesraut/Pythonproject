from django.contrib import admin

# Register your models here.
from .models import Category, Book, Writer

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','code','created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)


class WriterAdmin(admin.ModelAdmin):
    list_display = ('name','code','created_at', 'updated_at')


admin.site.register(Writer, WriterAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','code','created_at', 'updated_at')


admin.site.register(Book, BookAdmin)