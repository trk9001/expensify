from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from ..forms import CreateExpenseCategoryForm, CreateExpenseForm
from ..models import ExpenseCategory, Expense


class CreateExpenseCategoryView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    form_class = CreateExpenseCategoryForm
    template_name = 'core/expense/category/create.html'
    success_url = reverse_lazy('expense-category-list')

    def get_initial(self):
        current_user = self.request.user
        initial = {'user': current_user.pk}
        return initial


class ListExpenseCategoryView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = 'core/expense/category/list.html'


class CreateExpenseView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = CreateExpenseForm
    template_name = 'core/expense/create.html'
    success_url = reverse_lazy('index')  # TODO: Change

    def get_initial(self):
        current_user = self.request.user
        initial = {'user': current_user.pk}
        return initial
