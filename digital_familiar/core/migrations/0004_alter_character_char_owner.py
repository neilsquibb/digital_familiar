# Generated by Django 5.0.6 on 2024-06-30 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_name_character_char_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
