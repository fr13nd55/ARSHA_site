# Generated by Django 4.1.3 on 2022-11-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='rasm',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]
