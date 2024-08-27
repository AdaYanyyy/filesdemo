# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('files_id', models.AutoField(primary_key=True, serialize=False)),
                ('files_name', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('user_name', models.CharField(primary_key=True, max_length=32, serialize=False)),
                ('user_pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='files_user',
            field=models.ForeignKey(to='app01.userinfo'),
        ),
    ]
