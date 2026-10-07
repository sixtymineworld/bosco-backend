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

  rows = "".join(f"""
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.id}</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.name}</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.category}</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.material}</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.brand}</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{p.price} грн</td>
        </tr>
    """ for p in products)

  html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Склад: Спортивне спорядження</title>
    </head>
    <body style="font-family: Arial, sans-serif; padding: 24px;">
        <h2>Склад спортивного спорядження</h2>
        <p>Усього товарів у базі: <strong>{products.count()}</strong></p>
        <table style="border-collapse: collapse; width: 100%; max-width: 900px;">
            <thead>
                <tr style="background-color: #f4f4f4; text-align: left;">
                    <th style="border: 1px solid #ddd; padding: 8px;">ID</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Назва</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Категорія</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Матеріал</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Бренд</th>
                    <th style="border: 1px solid #ddd; padding: 8px;">Ціна</th>
                </tr>
            </thead>
            <tbody>
                {rows if rows else '<tr><td colspan="6" style="padding: 12px; text-align: center;">Товарів немає</td></tr>'}
            </tbody>
        </table>
    </body>
    </html>
    """
  return HttpResponse(html)


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