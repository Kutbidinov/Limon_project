from django.contrib import admin
from journal.models import Publication, Category, Hashtag, AboutMe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['topic', 'is_active']


@admin.register(AboutMe)
class AboutAdmin(admin.ModelAdmin):
    pass

