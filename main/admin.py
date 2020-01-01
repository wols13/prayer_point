from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin


class PrayerPointAdmin(ImportExportActionModelAdmin):
	pass

admin.site.register(PrayerPoint, PrayerPointAdmin)
admin.site.register(Category)