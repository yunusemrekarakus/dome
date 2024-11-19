# Generated by Django 5.1.2 on 2024-11-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_ekip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik1', models.CharField(max_length=200, verbose_name='Başlık 1')),
                ('baslik2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık 2')),
                ('icerik', models.TextField(verbose_name='İçerik')),
                ('button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Buton Metni')),
                ('button_link', models.URLField(blank=True, null=True, verbose_name='Yönlendirme Linki')),
                ('resim', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Resim')),
            ],
        ),
        migrations.AlterModelOptions(
            name='ekip',
            options={'verbose_name': 'Ekip', 'verbose_name_plural': 'Ekip'},
        ),
    ]
