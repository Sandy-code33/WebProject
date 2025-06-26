from django.db import models

class Order(models.Model):
 
     
    order_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.order_id} - {self.status}"
