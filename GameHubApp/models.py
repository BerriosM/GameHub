from django.db import models
from django.conf import settings

# Create your models here.

class Game(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='games')
	platform = models.CharField(max_length=100, blank=True)
	genre = models.CharField(max_length=100, blank=True)
	description = models.TextField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
	category = models.CharField(max_length=100, blank=True)
	image = models.CharField(max_length=255, blank=True, help_text='Ruta a la imagen (p. ej. img/blog-big/1.jpg)')
	excerpt = models.TextField(blank=True)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
	game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
	title = models.CharField(max_length=200)
	rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
	image = models.CharField(max_length=255, blank=True, help_text='Ruta a la imagen en static (p. ej. img/review/1.jpg)')
	excerpt = models.TextField(blank=True)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} ({self.rating})"


class Comment(models.Model):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100, blank=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Comment on {self.post.title} by {self.name or 'Anonymous'}"
