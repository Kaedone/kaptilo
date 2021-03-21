from django.contrib import admin
from .models import *


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["shortened", "uses", "user", "created"]
    list_filter = ["created"]
    search_fields = ["shortened", "link"]
