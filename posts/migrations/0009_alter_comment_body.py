# Generated by Django 5.0.6 on 2024-07-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=150),
        ),
    ]