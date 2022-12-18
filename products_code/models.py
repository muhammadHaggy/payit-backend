from django.db import models

# Create your models here.
class Products(models.Model):
    barcode = models.TextField(primary_key=True)
    nama_item = models.TextField()