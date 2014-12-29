# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trash', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('icon', models.ImageField(max_length=255, null=True, upload_to=b'pictures/%Y/%m/%d', blank=True)),
                ('slug', models.CharField(db_index=True, max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='extra',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name=b'articles', blank=True, to='blog.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
