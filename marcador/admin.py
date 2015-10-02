from django.contrib import admin

# Register your models here.

from .models import Bookmark, Tag #makes the classes in models



class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'is_updated')
    list_editable =('is_public',)
    list_filter = ('is_public', 'owner_username')
    search_fields = ['url', 'title', 'description']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
