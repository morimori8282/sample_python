# Generated by Django 2.2.5 on 2019-12-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahjongapp', '0003_auto_20191230_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventId', models.IntegerField()),
                ('roundId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]