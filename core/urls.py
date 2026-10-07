from django.contrib import admin
from django.urls import path
from warehouse.views import products_view, replenish_view, add_product_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", products_view, name="products_list"),
    path("products/add/", add_product_view, name="product_add"),
    path("replenish/<int:count>/", replenish_view, name="products_replenish"),
]