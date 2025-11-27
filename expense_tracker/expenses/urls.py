from django.urls import path
from . import views

urlpatterns = [
    path('expenses_list/', views.expenses_list, name = "expenses_list"),
    path('create_expenses/', views.create_expenses, name = "create_expenses"),
    path('update_expenses/<int:pk>/', views.update_expenses, name = "update_expenses"),
    path('delete_expenses/<int:pk>/', views.delete_expenses, name = "delete_expenses"),
]   