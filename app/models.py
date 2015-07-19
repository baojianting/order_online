from django.db import models

# Create your models here.
class Order(models.Model):
    product_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    province = models.CharField(max_length=200)
    detail_place = models.CharField(max_length=500)
    word = models.CharField(max_length=500)
