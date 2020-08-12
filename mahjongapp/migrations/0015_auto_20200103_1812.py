# Generated by Django 2.2.5 on 2020-01-03 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mahjongapp', '0014_auto_20200103_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdetailmodel',
            old_name='eventId',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventdetailmodel',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='eventmodel',
            old_name='winnerId',
            new_name='winner',
        ),
        migrations.RenameField(
            model_name='eventparticipantmodel',
            old_name='eventId',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventparticipantmodel',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='eventroundmodel',
            old_name='eventId',
            new_name='event',
        ),
    ]