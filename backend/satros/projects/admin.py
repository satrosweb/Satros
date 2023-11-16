from django.contrib import admin
from .models import Project, Category



@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'started', 'ended', 'created', 'updated']
    search_fields = ['title', 'status', 'category']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'started']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
