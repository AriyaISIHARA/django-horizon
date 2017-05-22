# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 08:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import horizon.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('egg', models.CharField(max_length=15)),
                ('sushi', models.CharField(default=None, max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('horizontal', horizon.manager.HorizontalManager()),
            ],
        ),
        migrations.CreateModel(
            name='HorizonChild',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            managers=[
                ('horizontal', horizon.manager.HorizontalManager()),
            ],
        ),
        migrations.CreateModel(
            name='HorizonParent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('spam', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('horizontal', horizon.manager.HorizontalManager()),
            ],
        ),
        migrations.CreateModel(
            name='HorizontalMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=15)),
                ('key', models.CharField(max_length=32)),
                ('index', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='horizontalmetadata',
            unique_together=set([('group', 'key')]),
        ),
        migrations.AddField(
            model_name='horizonchild',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.HorizonParent'),
        ),
        migrations.AddField(
            model_name='horizonchild',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='anothergroup',
            unique_together=set([('user', 'egg')]),
        ),
    ]
