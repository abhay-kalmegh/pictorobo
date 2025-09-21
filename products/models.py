from django.db import models
from ckeditor.fields import RichTextField  # Optional, for rich product descriptions
from categories.models import Category

# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)  # e.g., "Arduino Uno Starter Kit"
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=300, blank=True, null=True)
    description = RichTextField(blank=True, null=True)  # detailed specs, usage guide
    
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    brand = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Arduino", "Raspberry Pi"
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    gallery = models.JSONField(blank=True, null=True)  # store multiple images (or use a separate ProductImage model)

    specifications = models.JSONField(blank=True, null=True)  
    # Example: {"voltage": "5V", "current": "2A", "weight": "200g"}
    
    tags = models.CharField(max_length=200, blank=True, null=True)  
    # e.g., "arduino, robotics, beginner"
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name