from django.db import models

# Create your models here.

class Prayer_point(models.Model):
	content = models.TextField()

class Scripture(models.Model):
	book = models.CharField(max_length=255)
	chapter = models.IntegerField()
	verses = models.IntegerField()
	content = models.TextField()
	pid_list = models.ManyToManyField(Prayer_point)

class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=512)
	sid_list = models.ManyToManyField(Scripture)
