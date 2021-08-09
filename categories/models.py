from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return 'Category: ' + self.name
    
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"  
    


class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    category    = models.ForeignKey(
        'Category',
        related_name="products",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title