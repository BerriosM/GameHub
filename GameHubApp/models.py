from django.db import models

# Create your models here.

class Game(models.Model):
	title = models.CharField(max_length=200)
	platform = models.CharField(max_length=100, blank=True)
	genre = models.CharField(max_length=100, blank=True)
	description = models.TextField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
