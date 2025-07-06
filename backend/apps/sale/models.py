"""
Sale models for the application.
"""
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides self-updating created and modified fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(TimeStampedModel):
    """
    User role model.
    """
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'sale_role'
        
    def __str__(self):
        return self.name


class User(AbstractUser, TimeStampedModel):
    """
    Custom user model.
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_user'
        
    def __str__(self):
        return self.username


class Category(TimeStampedModel):
    """
    Product category model with hierarchical structure.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_categories')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_categories')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_category'
        verbose_name_plural = 'Categories'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    """
    Product model.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_products')
    deleted_at = models.DateTimeField(null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'sale_product'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.sku}"


class ProductImage(TimeStampedModel):
    """
    Product image model.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_product_images')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_product_images')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_product_image'
        
    def __str__(self):
        return f"Image for {self.product.name}"


class News(TimeStampedModel):
    """
    News model.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_news')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_news')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_news'
        verbose_name_plural = 'News'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class Promotion(TimeStampedModel):
    """
    Promotion model.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_promotions')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_promotions')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_promotion'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    """
    Comment and rating model.
    """
    TARGET_TYPE_CHOICES = [
        ('product', 'Product'),
        ('news', 'News'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    target_type = models.CharField(max_length=10, choices=TARGET_TYPE_CHOICES)
    target_id = models.BigIntegerField()
    rating = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    comment = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_comments')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_comments')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_comment'
        
    def __str__(self):
        return f"Comment by {self.user.username} on {self.target_type}"


class PromotionProduct(TimeStampedModel):
    """
    Promotion product relationship model.
    """
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='promotion_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promotion_products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_promotion_products')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_promotion_products')
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'sale_promotion_product'
        unique_together = ['promotion', 'product']
        
    def __str__(self):
        return f"{self.promotion.title} - {self.product.name}" 