from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'update_at', 'is_published', 'views', 'get_photo']
    search_fields = ['title']
    list_display_links = ['id', 'title']
    list_editable = ['is_published', 'views']
    list_filter = ('is_published', 'category')
    # fields =

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="90"')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управления новостями'
admin.site.site_header = 'Управления новостями'
