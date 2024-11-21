from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user')  # Display these fields in the list view
    search_fields = ('title', 'content')  # Allow searching by title or content

# Register the Note model with the custom admin class
admin.site.register(Note, NoteAdmin)
