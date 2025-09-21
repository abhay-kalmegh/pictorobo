from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "brand","price","discount_price","stock", "created_at")
    prepopulated_fields = {"slug": ("name",)}  # auto-fill slug from name