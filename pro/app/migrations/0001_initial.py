# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Computer_Science_Quiz_Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Computer Science Quiz Advance',
            },
        ),
        migrations.CreateModel(
            name='Computer_Science_Quiz_Beginners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
                ('start_count', models.SmallIntegerField(default=0)),
                ('max_counter', models.SmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Computer Science Quiz Beginners',
            },
        ),
        migrations.CreateModel(
            name='Computer_Science_Quiz_Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Computer Science Quiz Intermediate',
            },
        ),
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Correct',
            },
        ),
        migrations.CreateModel(
            name='Electronic_Principal_Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Electronic Principal Quiz',
            },
        ),
        migrations.CreateModel(
            name='Linux_Quiz_Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Linux Quiz Advance',
            },
        ),
        migrations.CreateModel(
            name='Linux_Quiz_Beginners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Linux Quiz Beginners',
            },
        ),
        migrations.CreateModel(
            name='Linux_Quiz_Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Linux Quiz Intermediate',
            },
        ),
        migrations.CreateModel(
            name='Networking_Quiz_Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Networking Quiz Advance',
            },
        ),
        migrations.CreateModel(
            name='Networking_Quiz_Beginners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Networking Quiz Beginners',
            },
        ),
        migrations.CreateModel(
            name='Networking_Quiz_Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=400)),
                ('choice1', models.CharField(blank=True, max_length=400)),
                ('choice2', models.CharField(blank=True, max_length=400)),
                ('choice3', models.CharField(blank=True, max_length=400)),
                ('choice4', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Networking Quiz Intermediate',
            },
        ),
        migrations.CreateModel(
            name='Stored_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Stored Answer',
            },
        ),
    ]
