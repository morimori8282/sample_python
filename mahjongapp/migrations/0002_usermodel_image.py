# Generated by Django 2.2.5 on 2019-12-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahjongapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(default='aaa', upload_to=''),
            preserve_default=False,
        ),
    ]