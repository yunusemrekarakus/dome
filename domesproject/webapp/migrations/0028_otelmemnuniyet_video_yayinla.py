# Generated by Django 5.1.2 on 2024-11-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_delete_hakkimda'),
    ]

    operations = [
        migrations.AddField(
            model_name='otelmemnuniyet',
            name='video_yayinla',
            field=models.BooleanField(default=False),
        ),
    ]