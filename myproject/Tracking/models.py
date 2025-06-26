from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order_id} - {self.status}"
