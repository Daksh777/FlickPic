# Generated by Django 5.0.6 on 2024-07-03 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]