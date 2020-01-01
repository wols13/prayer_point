from django.db import models

class PrayerPoint(models.Model):
    bible_ref = models.CharField(max_length=64, default="No Bible ref")
    scripture = models.TextField(max_length=2048, default="No scripture")
    content = models.TextField(max_length=2048, blank=False)
    category = models.TextField(max_length=128, blank=False)


class Category(models.Model):
    cat_id = models.CharField(max_length=3, blank=False, primary_key=True)
    name = models.CharField(max_length=32, blank=False)