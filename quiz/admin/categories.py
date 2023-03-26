from django.contrib import admin
from quiz.models.categories import *


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
