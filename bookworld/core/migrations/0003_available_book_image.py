# Generated by Django 2.2.14 on 2020-07-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_available_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_book',
            name='image',
            field=models.ImageField(default='None', upload_to=''),
        ),
    ]