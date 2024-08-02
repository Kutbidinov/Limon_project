from django.contrib import admin
<<<<<<< HEAD
from journal.models import Publication, Category, Hashtag
=======
from journal.models import Publication, Category, Hashtag, AboutMe
>>>>>>> 7ce1ef87fb7f7b02bd8ad0c3c6f8561e9259d45d

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['topic']
=======
    list_display = ['topic', 'is_active']


@admin.register(AboutMe)
class AboutAdmin(admin.ModelAdmin):
    pass
>>>>>>> 7ce1ef87fb7f7b02bd8ad0c3c6f8561e9259d45d

