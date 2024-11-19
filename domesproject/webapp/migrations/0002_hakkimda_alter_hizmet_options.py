# Generated by Django 5.1.2 on 2024-10-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hakkimda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('biyografi', models.TextField()),
                ('fotograf', models.ImageField(blank=True, null=True, upload_to='hakkimda_fotograflar/')),
            ],
            options={
                'verbose_name': 'Hakkımda',
                'verbose_name_plural': 'Hakkımda',
            },
        ),
        migrations.AlterModelOptions(
            name='hizmet',
            options={'verbose_name': 'Hizmet', 'verbose_name_plural': 'Hizmetler'},
        ),
    ]