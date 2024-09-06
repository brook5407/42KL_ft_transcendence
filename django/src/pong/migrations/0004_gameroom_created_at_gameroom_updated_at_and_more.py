# Generated by Django 5.0.3 on 2024-09-06 07:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0003_alter_gameroom_id_alter_matchhistory_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameroom',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='matchhistory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
