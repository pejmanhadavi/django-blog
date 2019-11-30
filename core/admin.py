from django.contrib import admin
from core import models

class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    list_display_links = ('slug',)
    list_editable = ('title',)

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(models.Article, AdminArticle)
admin.site.register(models.Category, AdminCategory)