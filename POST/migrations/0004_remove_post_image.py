# Generated by Django 4.2.13 on 2024-07-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0003_post_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
