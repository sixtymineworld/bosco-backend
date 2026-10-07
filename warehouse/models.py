from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=150, verbose_name="Назва")
  category = models.CharField(max_length=100, verbose_name="Категорія")
  material = models.CharField(max_length=100, verbose_name="Матеріал")
  brand = models.CharField(max_length=100, verbose_name="Бренд")
  price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name="Ціна"
  )

  def __str__(self):
    return f"{self.name} ({self.brand}) - {self.price} грн"