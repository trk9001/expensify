from django import forms

from ..models import ExpenseCategory, Expense


class CreateExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
        }


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
