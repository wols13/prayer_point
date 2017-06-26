from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    no_of_chapters = models.IntegerField(default=1)


class PrayerPoint(models.Model):
    book = models.IntegerField(default=1)
    chapter = models.IntegerField(default=1)
    verse = models.IntegerField(default=1)
    title = models.CharField(max_length=512, default="no_desc")
    content = models.TextField(max_length=512, default="no_content")


class Scripture(models.Model):
    book = models.CharField(max_length=20)
    chapter = models.IntegerField()
    verses = models.IntegerField()
    content = models.TextField()
    pid_list = models.ManyToManyField(PrayerPoint)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    sid_list = models.ManyToManyField(Scripture)
