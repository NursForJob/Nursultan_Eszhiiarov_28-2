from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
