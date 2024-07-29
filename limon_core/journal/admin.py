from django.contrib import admin
from journal.models import Publication, Category, Hashtag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['topic']

