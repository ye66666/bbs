# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_userprofile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('description', models.CharField(default=b'nothing....', max_length=255)),
                ('max_member_num', models.IntegerField(default=200)),
                ('admins', models.ManyToManyField(related_name='gruop_admins', to='web.UserProfile')),
                ('members', models.ManyToManyField(to='web.UserProfile', blank=True)),
            ],
        ),
    ]
