from django.db import models

# Create your models here.
class Feedback(models.Model):
    rating = models.IntegerField()
    remark = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating}"
