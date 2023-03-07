from django.urls import path

from .views import ProductDetailApiView


urlpatterns = [
    path('api/products/', ProductDetailApiView.as_view())
]
