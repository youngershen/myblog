# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141120_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trash', models.BooleanField(default=False)),
                ('name', models.CharField(default=b'unknown', max_length=255, null=True, blank=True)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(related_name=b'comments', to='blog.Article')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'contents',
            },
            bases=(models.Model,),
        ),
    ]
