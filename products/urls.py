from django.urls import path
from . import views as my_views

urlpatterns = [
    path('add_product/', my_views.add_products, name='add_product-url'),
    path('product/', my_views.products, name='product-url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_product, name='update-url'),
    path('pay/<id>', my_views.pay, name='pay-url'),
]
