# Generated by Django 4.2.16 on 2025-02-25 05:53

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_alter_blog_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=models.CharField(max_length=100), unique=True),
        ),
    ]
