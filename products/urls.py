from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
   path('', ProductsListView.as_view(), name='index'),
   path('<int:category_id>/', ProductsListView.as_view(), name='category'),
   path('page/<int:page>/', ProductsListView.as_view(), name='page'),
   path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
   path('basket_delete/<int:id>/', basket_delete, name='basket_delete')
   ]