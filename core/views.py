from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Category, Subcategory, TransactionType, Transaction, Status
from .serializers import CategorySerializer, SubcategorySerializer


# API для AJAX
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        t_type = self.request.query_params.get('transaction_type')
        if t_type: queryset = queryset.filter(transaction_type_id=t_type)
        return queryset


class SubcategoryListView(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        queryset = Subcategory.objects.all()
        cat = self.request.query_params.get('category')
        if cat: queryset = queryset.filter(category_id=cat)
        return queryset


# Главная + Фильтрация
def index(request):
    transactions = Transaction.objects.all().order_by('-date')

    # Фильтры
    if request.GET.get('date_from'): transactions = transactions.filter(date__gte=request.GET.get('date_from'))
    if request.GET.get('date_to'): transactions = transactions.filter(date__lte=request.GET.get('date_to'))
    if request.GET.get('status'): transactions = transactions.filter(status_id=request.GET.get('status'))
    if request.GET.get('type'): transactions = transactions.filter(transaction_type_id=request.GET.get('type'))
    if request.GET.get('category'): transactions = transactions.filter(category_id=request.GET.get('category'))

    return render(request, 'core/index.html', {
        'transactions': transactions,
        'statuses': Status.objects.all(),
        'types': TransactionType.objects.all()
    })


# Создание и Редактирование
def transaction_form(request, pk=None):
    transaction = get_object_or_404(Transaction, pk=pk) if pk else None

    if request.method == "POST":
        data = {
            'status_id': request.POST.get('status'),
            'transaction_type_id': request.POST.get('type'),
            'category_id': request.POST.get('category'),
            'subcategory_id': request.POST.get('subcategory'),
            'amount': request.POST.get('amount'),
            'comment': request.POST.get('comment'),
        }
        if transaction:
            for attr, value in data.items(): setattr(transaction, attr, value)
            transaction.save()
        else:
            Transaction.objects.create(**data)
        return redirect('index')

    return render(request, 'core/form.html', {
        'transaction': transaction,
        'types': TransactionType.objects.all(),
        'statuses': Status.objects.all()
    })


# Удаление
def transaction_delete(request, pk):
    get_object_or_404(Transaction, pk=pk).delete()
    return redirect('index')