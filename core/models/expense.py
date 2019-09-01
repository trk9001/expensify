import datetime

from django.contrib.auth.models import User
from django.db import models


class ExpenseCategory(models.Model):
    """User-defined expense category."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expense_categories',
        related_query_name='expense_category',
    )
    name = models.CharField(
        help_text='The category\'s name',
        max_length=200,
    )
    description = models.TextField(
        help_text='A brief description of the category',
        max_length=500,
        blank=True,
    )
    hidden = models.BooleanField(
        help_text='Whether this category will be hidden',
        default=False,
    )

    class Meta:
        verbose_name_plural = 'expense categories'

    def __str__(self):
        return f'{self.user} > {self.name}'


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expenses',
        related_query_name='expense',
    )
    category = models.ForeignKey(
        ExpenseCategory,
        help_text='Select an expense category',
        on_delete=models.SET_NULL,
        related_name='expenses',
        related_query_name='expense',
        null=True,
    )
    description = models.CharField(
        help_text='Description of the expense',
        max_length=200,
    )
    amount = models.DecimalField(
        help_text='The amount of money spent',
        decimal_places=2,
        max_digits=12,
    )
    date = models.DateField(
        help_text='Date of the expense',
        default=datetime.date.today,
    )
    tags = models.CharField(
        help_text='Comma-separated tags for this expense',
        max_length=500,
        blank=True,
    )

    def __str__(self):
        return f'{self.category} > {self.description} ({self.amount})'
