from django.contrib import admin
from .models import TrasnporterDetails

@admin.register(TrasnporterDetails)
class TrasnporterAdmin(admin.ModelAdmin):
	list_display = ("name", "gst_no")
	list_filter = ("name",)
	search_fields = ("name",)