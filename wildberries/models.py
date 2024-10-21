from django.db import models


class Product(models.Model):
    article = models.IntegerField()
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    basic_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    total_quantity = models.IntegerField()
    review_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
