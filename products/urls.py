from django.contrib import admin
from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addproduct/', views.addProduct, name="addproduct"),
    path('products/<int:id>', views.detail, name="product_detail"),
    path('update/<int:id>', views.updateProduct, name="update"),
    path('delete/<int:id>', views.deleteProduct, name="delete"),
    path('', views.products, name="products"),

]
