# Generated by Django 4.1.3 on 2022-11-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/products/'),
        ),
    ]
