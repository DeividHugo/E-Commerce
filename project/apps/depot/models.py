from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='static/media/products/', height_field=None, width_field=None)
    price = models.FloatField()
    description = models.CharField(max_length=280)
    inventory = models.IntegerField()

    def __str__(self):
        return self.name
