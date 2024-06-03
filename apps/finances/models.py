from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=25)
    rate = models.FloatField()

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.FloatField()

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'


class Category(models.Model):
    name = models.CharField(max_length=250)
    plan = models.FloatField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
