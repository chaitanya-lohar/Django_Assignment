from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=100,default='')
    weight=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

    def __str__(self):
        return self.name