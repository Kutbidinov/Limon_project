from django.contrib import admin
from journal.models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass

