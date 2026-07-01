from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/categories/', CategoryListView.as_view()),
    path('api/subcategories/', SubcategoryListView.as_view()),
    path('create/', transaction_form, name='transaction-create'),
    path('update/<int:pk>/', transaction_form, name='transaction-update'),
    path('delete/<int:pk>/', transaction_delete, name='transaction-delete'),
]