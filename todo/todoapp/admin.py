from todoapp.models import *
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
	list_display = ["name", "priority", "difficulty", "created", "done"]
	search_fields = ["name"]

admin.site.register(Item, ItemAdmin)