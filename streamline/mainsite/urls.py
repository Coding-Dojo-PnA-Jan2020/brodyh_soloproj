from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products_index),
    path('products/<int:pk>', views.products_show),
    path('products/<int:pk>/edit', views.products_edit),
    path('products/<int:pk>/delete', views.products_delete),
    path('products/new', views.products_new),
    path('vendors/', views.vendor_index),
    path('vendors/signup', views.vendor_signup),
]