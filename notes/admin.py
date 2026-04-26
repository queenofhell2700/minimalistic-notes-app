from django.contrib import admin
from .models import Note, Tag

# 1. Register Tag normally
admin.site.register(Tag)

# 2. Use ONLY the decorator for Note (Delete any other register lines for Note)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'priority', 'is_done', 'created_at')
    list_filter = ('priority', 'is_done')