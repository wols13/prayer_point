from django.contrib import admin

# Register your models here.

from .models import Prayer_point
from .models import Scripture
from .models import Category

admin.site.register(Prayer_point)
admin.site.register(Scripture)
admin.site.register(Category)
