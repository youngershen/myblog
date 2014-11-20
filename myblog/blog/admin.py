from django.contrib import admin
from blog.models import Tag
from blog.models import Article
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
