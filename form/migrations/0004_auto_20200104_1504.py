# Generated by Django 2.2 on 2020-01-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20200104_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='email',
        ),
        migrations.RemoveField(
            model_name='form',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='form',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='form',
            name='other_network',
        ),
        migrations.RemoveField(
            model_name='form',
            name='past_experience',
        ),
        migrations.RemoveField(
            model_name='form',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='form',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='form',
            name='title',
        ),
        migrations.RemoveField(
            model_name='form',
            name='traffic_source',
        ),
        migrations.RemoveField(
            model_name='form',
            name='traffic_volume',
        ),
        migrations.RemoveField(
            model_name='form',
            name='vertical_type',
        ),
        migrations.RemoveField(
            model_name='form',
            name='where_here_about_advbuzz',
        ),
    ]
