from django.contrib import admin

# Register your models here.

from .models import Book
from .models import Chapter
from .models import PrayerPoint
from .models import Scripture
from .models import Category

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(PrayerPoint)
admin.site.register(Scripture)
admin.site.register(Category)
