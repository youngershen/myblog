from django.contrib import admin
from blog.models import Tag
from blog.models import Article
from blog.models import Comment
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
