from django.urls import path
from .views import (
    ProductDetailView, 
    ProductCreateView,
    ProductListCreateApiView,
    ProductUpdateApiView,
    ProductDeleteApiView,
    ProductMixinView, 
    alt_view
)


urlpatterns = [
    path('<int:pk>/', ProductMixinView.as_view(), name='product-detail'),
    path('', ProductListCreateApiView.as_view()),
    path('<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDeleteApiView.as_view()),
]

