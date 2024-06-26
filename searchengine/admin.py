from django.contrib import admin
from .models import Websites
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Websites)
class SearchDataAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'rank', 'title', 'url']