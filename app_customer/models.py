from django.db import models


class Customer(models.Model):
    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    name = models.CharField(max_length=100)
    address = models.TextField()
