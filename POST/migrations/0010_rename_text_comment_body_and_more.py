# Generated by Django 4.2.13 on 2024-07-11 09:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0009_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modified',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='POST.post'),
        ),
    ]
