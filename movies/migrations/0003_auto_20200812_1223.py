# Generated by Django 3.1 on 2020-08-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200812_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
