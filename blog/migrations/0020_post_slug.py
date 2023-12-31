# Generated by Django 3.2.20 on 2023-07-21 06:32

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
    ]
