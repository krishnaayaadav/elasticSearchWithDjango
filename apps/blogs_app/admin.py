from django.contrib import admin
from apps.blogs_app.models import Blog


@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ['title' , 'category', 'author', 'created', 'description']