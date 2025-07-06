"""
Celery tasks for sale app.
"""
import logging
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Product

logger = logging.getLogger(__name__)


@shared_task
def check_low_stock_products():
    """
    Check for products with low stock and send notification.
    """
    try:
        low_stock_threshold = 10
        low_stock_products = Product.objects.filter(
            stock_quantity__lte=low_stock_threshold,
            is_active=True
        )
        
        if low_stock_products.exists():
            subject = "Low Stock Alert"
            message = f"""
            The following products have low stock:
            
            """
            
            for product in low_stock_products:
                message += f"- {product.name} (SKU: {product.sku}): {product.stock_quantity} units\n"
            
            message += "\nPlease restock these products soon."
            
            # Send to admin email (you can configure this in settings)
            admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@example.com')
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin_email],
                fail_silently=False,
            )
            
            logger.info(f"Low stock alert sent for {low_stock_products.count()} products")
            return True
        else:
            logger.info("No low stock products found")
            return True
            
    except Exception as e:
        logger.error(f"Failed to check low stock products: {e}")
        return False


@shared_task
def send_new_product_notification(product_id):
    """
    Send notification when a new product is added.
    """
    try:
        product = Product.objects.get(id=product_id)
        
        subject = f"New Product Added: {product.name}"
        message = f"""
        A new product has been added to our catalog:
        
        Product Details:
        - Name: {product.name}
        - SKU: {product.sku}
        - Price: ${product.price}
        - Category: {product.category.name}
        - Stock: {product.stock_quantity} units
        
        Product Description:
        {product.description}
        
        Best regards,
        SellApp Team
        """
        
        # Send to admin email
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@example.com')
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email],
            fail_silently=False,
        )
        
        logger.info(f"New product notification sent for product #{product.id}")
        return True
        
    except Product.DoesNotExist:
        logger.error(f"Product #{product_id} not found")
        return False
    except Exception as e:
        logger.error(f"Failed to send new product notification: {e}")
        return False


@shared_task
def send_product_update_notification(product_id):
    """
    Send notification when a product is updated.
    """
    try:
        product = Product.objects.get(id=product_id)
        
        subject = f"Product Updated: {product.name}"
        message = f"""
        A product has been updated in our catalog:
        
        Product Details:
        - Name: {product.name}
        - SKU: {product.sku}
        - Price: ${product.price}
        - Category: {product.category.name}
        - Stock: {product.stock_quantity} units
        
        Product Description:
        {product.description}
        
        Best regards,
        SellApp Team
        """
        
        # Send to admin email
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@example.com')
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email],
            fail_silently=False,
        )
        
        logger.info(f"Product update notification sent for product #{product.id}")
        return True
        
    except Product.DoesNotExist:
        logger.error(f"Product #{product_id} not found")
        return False
    except Exception as e:
        logger.error(f"Failed to send product update notification: {e}")
        return False 