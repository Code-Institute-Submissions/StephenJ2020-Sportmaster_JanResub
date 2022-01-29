from django.contrib import admin
from .models import Announcements, Post


class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'blurb',
        'image',
        'date_added',
        'author'
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Announcements, AnnouncementsAdmin)
