# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141120_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name=b'articles', null=True, to=b'blog.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='icon',
            field=models.ImageField(max_length=255, null=True, upload_to=b'pictures/%Y/%m/%d', blank=True),
        ),
    ]
