from django.db import models

# Create your models here.

class İHA(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=30, blank=True, null=True, default="")
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    

    def __str__(self):
        return f"{self.brand} - {self.model}"

