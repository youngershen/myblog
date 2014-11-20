# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trash', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(null=True, blank=True)),
                ('slug', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trash', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
                ('extra', models.TextField(null=True, blank=True)),
                ('icon', models.ImageField(max_length=255, upload_to=b'pictures/%Y/%m/%d')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name=b'articles', to='blog.Tag'),
            preserve_default=True,
        ),
    ]
