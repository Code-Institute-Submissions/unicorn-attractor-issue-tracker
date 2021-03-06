# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('IC', 'Incomplete'), ('IP', 'Inprogress'), ('CP', 'Complete')], default='IC', max_length=2)),
                ('issue_type', models.CharField(choices=[('BG', 'Bug'), ('FR', 'Feature')], default='BG', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='issues.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issues.Issue'),
        ),
    ]
