# Generated by Django 3.1.4 on 2020-12-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
