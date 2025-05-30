# Generated by Django 4.2.16 on 2025-02-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='blog_images/')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
