from django.db import models

def upload_to(instance, filename):
  return 'product-images/product-{product_name}-img.jpeg'.format(product_name=instance.name)

class Category(models.Model):
  name = models.TextField(max_length=255)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.TextField(max_length=255)
  image = models.ImageField(upload_to=upload_to, blank=True, null=True)
  barcode = models.TextField(max_length=255)
  price = models.DecimalField(max_digits=9,decimal_places=2)
  net_weight = models.TextField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
  flavor = models.TextField(max_length=255)
  alcohol_content = models.TextField(max_length=255)
  current_stock = models.IntegerField()

  def __str__(self):
    return self.name


class Purchase(models.Model):
  pass