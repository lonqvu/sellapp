"""
Signals for sale app.
"""
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Product, News, Promotion, Comment, Category


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    """
    Handle post-save events for Product model.
    """
    # Clear product cache when product is updated
    cache.delete(f'product_{instance.id}')
    cache.delete('products_list')
    
    if created:
        # Log new product creation
        print(f"New product created: {instance.name} (SKU: {instance.sku})")
    else:
        # Log product update
        print(f"Product updated: {instance.name} (SKU: {instance.sku})")


@receiver(post_save, sender=Category)
def category_post_save(sender, instance, created, **kwargs):
    """
    Handle post-save events for Category model.
    """
    # Clear category cache
    cache.delete(f'category_{instance.id}')
    cache.delete('categories_list')
    
    if created:
        print(f"New category created: {instance.name}")
    else:
        print(f"Category updated: {instance.name}")


@receiver(post_save, sender=News)
def news_post_save(sender, instance, created, **kwargs):
    """
    Handle post-save events for News model.
    """
    # Clear news cache
    cache.delete(f'news_{instance.id}')
    cache.delete('news_list')
    
    if created:
        print(f"New news article published: {instance.title}")
    else:
        print(f"News article updated: {instance.title}")


@receiver(post_save, sender=Promotion)
def promotion_post_save(sender, instance, created, **kwargs):
    """
    Handle post-save events for Promotion model.
    """
    # Clear promotion cache
    cache.delete(f'promotion_{instance.id}')
    cache.delete('promotions_list')
    
    if created:
        print(f"New promotion created: {instance.title}")
    else:
        print(f"Promotion updated: {instance.title}")


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created, **kwargs):
    """
    Handle post-save events for Comment model.
    """
    if created:
        # Log new comment
        print(f"New comment by {instance.user.username} on {instance.target_type} #{instance.target_id}")
        
        # Clear related cache
        cache.delete(f'{instance.target_type}_{instance.target_id}_comments')
        cache.delete(f'{instance.target_type}_{instance.target_id}_rating')
    else:
        print(f"Comment updated by {instance.user.username}")


@receiver(post_delete, sender=Product)
def product_post_delete(sender, instance, **kwargs):
    """
    Handle post-delete events for Product model.
    """
    # Clear product cache
    cache.delete(f'product_{instance.id}')
    cache.delete('products_list')
    print(f"Product deleted: {instance.name} (SKU: {instance.sku})")


@receiver(post_delete, sender=Category)
def category_post_delete(sender, instance, **kwargs):
    """
    Handle post-delete events for Category model.
    """
    # Clear category cache
    cache.delete(f'category_{instance.id}')
    cache.delete('categories_list')
    print(f"Category deleted: {instance.name}")


@receiver(post_delete, sender=News)
def news_post_delete(sender, instance, **kwargs):
    """
    Handle post-delete events for News model.
    """
    # Clear news cache
    cache.delete(f'news_{instance.id}')
    cache.delete('news_list')
    print(f"News article deleted: {instance.title}")


@receiver(post_delete, sender=Promotion)
def promotion_post_delete(sender, instance, **kwargs):
    """
    Handle post-delete events for Promotion model.
    """
    # Clear promotion cache
    cache.delete(f'promotion_{instance.id}')
    cache.delete('promotions_list')
    print(f"Promotion deleted: {instance.title}")


@receiver(post_delete, sender=Comment)
def comment_post_delete(sender, instance, **kwargs):
    """
    Handle post-delete events for Comment model.
    """
    # Clear related cache
    cache.delete(f'{instance.target_type}_{instance.target_id}_comments')
    cache.delete(f'{instance.target_type}_{instance.target_id}_rating')
    print(f"Comment deleted by {instance.user.username}") 