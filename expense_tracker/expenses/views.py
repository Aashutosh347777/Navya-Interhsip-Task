from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense
from decimal import Decimal

# Create your views here.
@login_required
def expenses_list(request):
    user_expenses = Expense.objects.filter(user=request.user).order_by('-date')

    context = {
        'expenses': user_expenses
    }

    return render(request, 'expenses/expenses_list.html', context)

@login_required
def create_expenses(request):
    if request.method == "POST":
        title = request.POST.get('title')
        amount_str = request.POST.get('amount')
        category = request.POST.get('category')
        date_str = request.POST.get('date')

        amount = Decimal(amount_str)

        if amount <= 0:
            messages.error(request, "Amount must be greater than zero.")
            return redirect('create_expenses')
        
        try:
            Expense.objects.create(
                user=request.user,      
                title=title,
                amount=amount,
                category=category,
                date=date_str
            )
            
            messages.success(request, "Expense added successfully!")
            return redirect('expenses_list')
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            return redirect('create_expenses')

    else:  
        return render(request, 'expenses/create_expenses.html')

@login_required
def update_expenses(request,pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == "POST":
        title = request.POST.get('title')
        amount_str = request.POST.get('amount')
        category = request.POST.get('category')
        date_str = request.POST.get('date')

        amount = Decimal(amount_str)

        if amount <= 0:
            messages.error(request, "Amount must be greater than zero.")
            return redirect('update_expenses', expense_id=expense.id)

        
        try:
            expense.title = title
            expense.amount = amount
            expense.category = category
            expense.date = date_str
            expense.save()
            
            messages.success(request, "Expense updated successfully!")
            return redirect('expenses_list')
        
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            return redirect('create_expenses')
        
    else:
        context = {
            'expense': expense
        }
        return render(request, 'expenses/update_expenses.html', context)


@login_required
def delete_expenses(request,pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == "POST":
        title = expense.title # saving title for the success message
        try:
            expense.delete()
            messages.success(request, f"Expense '{title}' was successfully deleted.")
            return redirect('expenses_list')
        except Exception as e:
            messages.error(request, f"An error occurred while deleting the expense: {e}")
            return redirect('expenses_list')

    context = {
        'expense': expense
    }
    return render(request, 'expenses/delete_expenses.html',context)
