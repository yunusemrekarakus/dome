# Generated by Django 5.1.2 on 2024-11-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_contact_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='is_read',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
