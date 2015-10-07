# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
>>>>>>> b13cbb0db4ca8e0d6810ffcb15b01665d68d4abc
                ('url', models.URLField()),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_public', models.BooleanField(verbose_name='public', default=True)),
                ('date_created', models.DateTimeField(verbose_name='date_created')),
                ('date_updated', models.DateTimeField(verbose_name='date_updated')),
<<<<<<< HEAD
                ('owner', models.ForeignKey(related_name='bookmarks', verbose_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
=======
                ('owner', models.ForeignKey(verbose_name='owner', related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'bookmarks',
                'verbose_name': 'bookmark',
>>>>>>> b13cbb0db4ca8e0d6810ffcb15b01665d68d4abc
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
=======
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'tags',
                'verbose_name': 'tag',
>>>>>>> b13cbb0db4ca8e0d6810ffcb15b01665d68d4abc
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
<<<<<<< HEAD
            field=models.ManyToManyField(blank=True, to='marcador.Tag'),
=======
            field=models.ManyToManyField(to='marcador.Tag', blank=True),
>>>>>>> b13cbb0db4ca8e0d6810ffcb15b01665d68d4abc
        ),
    ]
