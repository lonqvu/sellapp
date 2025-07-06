"""
URL configuration for sale app.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'sale'

router = DefaultRouter()
router.register(r'roles', views.RoleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'product-images', views.ProductImageViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'promotion-products', views.PromotionProductViewSet)

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('', include(router.urls)),
] 