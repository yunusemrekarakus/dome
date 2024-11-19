# Generated by Django 5.1.2 on 2024-11-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('cover_image', models.ImageField(upload_to='video_covers/', verbose_name='Kapak Görseli')),
                ('video_url', models.URLField(help_text="Video dosyasının URL'si", verbose_name='Video URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Video Galeri',
                'verbose_name_plural': 'Video Galeri',
                'ordering': ['-created_at'],
            },
        ),
    ]
