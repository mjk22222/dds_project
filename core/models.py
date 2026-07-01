from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Статус")
    # Бизнес, Личное, Налог


class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тип")
    # Пополнение, Списание


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    # Привязка категории к типу (Бизнес-правило из ТЗ)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name='categories')


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Подкатегория")
    # Привязка подкатегории к категории
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')


class Transaction(models.Model):
    # Дата по умолчанию сегодня, но можно менять (как в ТЗ)
    date = models.DateField(default=timezone.now, verbose_name="Дата создания")

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегория")

    # Сумма обязательна
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма")
    # Комментарий необязателен (blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")