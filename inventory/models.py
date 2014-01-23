from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=128, unique=True)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name
