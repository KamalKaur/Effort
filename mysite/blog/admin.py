from django.contrib import admin
from blog.models import *
from django.shortcuts import render_to_response, get_object_or_404

class BlogAdmin(admin.ModelAdmin):
    # exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
