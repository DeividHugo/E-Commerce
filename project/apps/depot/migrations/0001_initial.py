# Generated by Django 4.1.3 on 2022-11-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to=None)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=280)),
                ('inventory', models.IntegerField()),
            ],
        ),
    ]
