"""
Views for sale app.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Category, Product, Role, User, ProductImage, News, Promotion, Comment, PromotionProduct
from .serializers import (
    CategorySerializer, ProductSerializer, RoleSerializer, UserSerializer,
    ProductImageSerializer, NewsSerializer, PromotionSerializer, CommentSerializer,
    PromotionProductSerializer
)


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check endpoint for monitoring.
    """
    return Response(
        {
            'status': 'healthy',
            'message': 'SellApp service is running',
        },
        status=status.HTTP_200_OK
    )


class RoleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Role model.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    """
    queryset = User.objects.all().select_related('role')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['role', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username', 'created_at']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Category model.
    """
    queryset = Category.objects.all().select_related('parent', 'created_by')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['parent', 'created_by']
    search_fields = ['name', 'slug']
    ordering_fields = ['name', 'created_at']


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product model.
    """
    queryset = Product.objects.all().select_related('category', 'created_by')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['category', 'is_active', 'price', 'created_by']
    search_fields = ['name', 'description', 'sku', 'slug']
    ordering_fields = ['name', 'price', 'created_at']

    @action(detail=True, methods=['post'])
    def update_stock(self, request, pk=None):
        """Update product stock quantity."""
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        
        if quantity < 0:
            return Response(
                {'error': 'Quantity cannot be negative'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        product.stock_quantity = quantity
        product.save()
        
        return Response(
            {'message': f'Stock updated to {quantity}'},
            status=status.HTTP_200_OK
        )


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ProductImage model.
    """
    queryset = ProductImage.objects.all().select_related('product', 'created_by')
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['product', 'created_by']
    search_fields = ['product__name']
    ordering_fields = ['created_at']


class NewsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for News model.
    """
    queryset = News.objects.all().select_related('created_by')
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['created_by']
    search_fields = ['title', 'content', 'slug']
    ordering_fields = ['title', 'created_at']


class PromotionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Promotion model.
    """
    queryset = Promotion.objects.all().select_related('created_by')
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['start_date', 'end_date', 'created_by']
    search_fields = ['title', 'description', 'slug']
    ordering_fields = ['title', 'start_date', 'created_at']


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Comment model.
    """
    queryset = Comment.objects.all().select_related('user', 'created_by')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['target_type', 'rating', 'user', 'created_by']
    search_fields = ['user__username', 'comment']
    ordering_fields = ['created_at', 'rating']


class PromotionProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for PromotionProduct model.
    """
    queryset = PromotionProduct.objects.all().select_related('promotion', 'product', 'created_by')
    serializer_class = PromotionProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['promotion', 'product', 'created_by']
    search_fields = ['promotion__title', 'product__name']
    ordering_fields = ['created_at'] 