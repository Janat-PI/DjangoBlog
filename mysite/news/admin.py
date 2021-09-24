from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'update_at', 'is_published', 'views']
    search_fields = ['title']
    list_display_links = ['id', 'title']
    list_editable = ['is_published', 'views']
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
