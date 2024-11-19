# Generated by Django 5.1.2 on 2024-10-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_hakkimda_alter_hizmet_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtelMemnuniyet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musteri_adi', models.CharField(max_length=200)),
                ('yorum', models.TextField(blank=True, null=True)),
                ('yildiz', models.IntegerField(choices=[(5, '5 - Mükemmel'), (4, '4 - Çok İyi'), (3, '3 - İyi'), (2, '2 - Orta'), (1, '1 - Kötü')])),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('onayli', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Otel Memnuniyeti',
                'verbose_name_plural': 'Otel Memnuniyetleri',
            },
        ),
    ]