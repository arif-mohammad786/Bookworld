# Generated by Django 2.2.14 on 2020-07-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_available_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='available_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.TextField(max_length=100)),
            ],
        ),
    ]
