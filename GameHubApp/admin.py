from django.contrib import admin
from .models import BlogPost, Game


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'created_at')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'platform', 'genre', 'created_at')

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('title', 'game', 'rating', 'created_at')
