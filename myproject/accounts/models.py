from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     mobile = models.CharField(max_length=15, unique=True)

# class Feedback(models.Model):
#     rating = models.IntegerField()
#     remark = models.TextField()

#     def __str__(self):
#         return f"Rating: {self.rating}"
    
from django.db import models

class Feedback(models.Model):
    rating = models.IntegerField()
    remark = models.TextField()

    def __str__(self):
        return f"{self.rating} - {self.remark[:20]}"
    
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_image = models.CharField(max_length=255, blank=True)  # store static path
    # product_image = models.ImageField(upload_to='products/')
    product_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name

