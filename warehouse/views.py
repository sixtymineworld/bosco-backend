from django.shortcuts import render
import random
from django.http import HttpResponse
from .models import Product

# Create your views here.

NAMES = [
    "М’яч футбольний",
    "Ракетка тенісна",
    "Шолом захисний",
    "Килимок тренувальний",
    "Еспандер",
    "Гантель 5кг",
    "Щитки гомілкові",
    "Пояс атлетичний",
    "Окуляри для плавання",
    "Скакалка швидкісна",
]
CATEGORIES = [
    "Футбол",
    "Теніс",
    "Фітнес",
    "Плавання",
    "Силовий спорт",
    "Зимовий спорт",
]
MATERIALS = [
    "Синтетична шкіра",
    "Графіт",
    "Алюміній",
    "Поліестер",
    "Гума",
    "Силікон",
]
BRANDS = [
    "Nike",
    "Adidas",
    "Wilson",
    "Puma",
    "Reebok",
    "Under Armour",
    "Salomon",
]


def products_view(request):
  products = Product.objects.all()
  return render(request, "warehouse/products.html", {"products": products})



def replenish_view(request, count: int):
  if count <= 0:
    return HttpResponse("Кількість має бути більшою за 0.", status=400)

  new_items = [
      Product(
          name=random.choice(NAMES),
          category=random.choice(CATEGORIES),
          material=random.choice(MATERIALS),
          brand=random.choice(BRANDS),
          price=round(random.uniform(250.0, 5000.0), 2),
      )
      for _ in range(count)
  ]

  Product.objects.bulk_create(new_items)
  return HttpResponse(f"Додано {count} нових записів")