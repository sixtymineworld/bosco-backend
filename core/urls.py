from django.contrib import admin
from django.urls import path
from warehouse.views import products_view, replenish_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", products_view, name="products_list"),
    path("replenish/<int:count>/", replenish_view, name="products_replenish"),
]