from django.db import models
from django.core.urlresolvers import reverse
from core.models import Entity
from unidecode import unidecode
import time
# Create your models here.

class Tag(Entity):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    extra = models.TextField(null=True, blank=True)
    icon = models.ImageField(max_length=255, upload_to='pictures/%Y/%m/%d', null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = '-'.join(unidecode(unicode(self.name)).lower().split())
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering=['-created_at']
        verbose_name='tag'
        verbose_name_plural='tags'


class Article(Entity):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True, default='')
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.slug = '-'.join(unidecode(unicode(self.title)).lower().split()) + '-' 
        self.slug += time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug':self.slug})

    class Meta:
        ordering=['-created_at']
        verbose_name='article'
        verbose_name_plural='articles'

class Comment(Entity):
    name = models.CharField(max_length=255, null=True, blank=True,default='unknown')
    content = models.TextField()
    article = models.ForeignKey(Article, related_name='comments')

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.__unicode__()

    class Meta:
        ordering=['-created_at']
        verbose_name='comment'
        verbose_name_plural='contents'


