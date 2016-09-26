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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('head_img', models.ImageField(upload_to=b'uploads')),
                ('summary', models.CharField(max_length=255)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('hidden', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=1000, verbose_name='\u4f18\u5148\u7ea7')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='web.Article')),
                ('parent_comment', models.ForeignKey(related_name='p_comment', blank=True, to='web.Comment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThumbUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='web.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('groups', models.ManyToManyField(to='web.UserGroup')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thumbup',
            name='user',
            field=models.ForeignKey(to='web.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='web.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='admin',
            field=models.ManyToManyField(to='web.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='web.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='categroy',
            field=models.ForeignKey(verbose_name='\u677f\u5757', to='web.Category'),
            preserve_default=True,
        ),
    ]
