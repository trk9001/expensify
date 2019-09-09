from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('expenses/new/', views.CreateExpenseView.as_view(), name='new-expense'),
    path('expenses/categories/new/', views.CreateExpenseCategoryView.as_view(), name='new-expense-category'),
]
