from django.contrib import admin
from .models import BlogPost, Game
from .models import Review, Comment


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'name', 'created_at')
	list_filter = ('created_at',)
