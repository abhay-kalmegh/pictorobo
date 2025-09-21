from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)   # e.g., "Robotics Kits", "Sensors", "Motors"
    slug = models.SlugField(max_length=150, unique=True)   # SEO-friendly URL
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="subcategories"
    )  # for nested categories like "Sensors > IR Sensors"
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def _str_(self):
        return self.name