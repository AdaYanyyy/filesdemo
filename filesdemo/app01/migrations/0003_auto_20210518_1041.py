# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210518_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='files_name',
            field=models.FileField(upload_to='media'),
        ),
    ]
