# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foo_app', '0002_auto_20151121_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='foo',
            name='text',
            field=models.TextField(),
        ),
    ]
