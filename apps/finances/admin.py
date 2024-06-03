from django.contrib import admin
from apps.finances import models


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('owner', 'currency', 'balance')
    fields = ('owner', 'currency', 'balance')


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')
    fields = ('name', 'rate')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'plan')
    fields = ('name', 'plan')


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('category', 'account', 'amount')
    fields = ('category', 'account', 'amount')
