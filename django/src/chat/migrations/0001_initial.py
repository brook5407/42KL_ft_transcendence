# Generated by Django 5.0.3 on 2024-09-12 03:02

import base.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', base.fields.RandomStringIDField(editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', base.fields.RandomStringIDField(editable=False, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=False)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='chatroom_covers/')),
                ('is_group_chat', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(blank=True, related_name='chatroom_members', to=settings.AUTH_USER_MODEL)),
                ('messages', models.ManyToManyField(related_name='chatroom_messages', to='chat.chatmessage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chat.chatroom'),
        ),
        migrations.CreateModel(
            name='ActiveChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom')),
            ],
        ),
    ]
