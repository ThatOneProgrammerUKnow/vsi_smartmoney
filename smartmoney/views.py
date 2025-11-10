from django.shortcuts import render, redirect
from .forms import CategoryForm, TransactionForm
from .models import Category, Transaction
from django.contrib.auth.decorators import login_required

#===# Switch between pages #===#
def dashboard(request):
    return render(request, 'apps/smartmoney/dashboard.html')

## Displays transactions ##
def transaction(request):
    transactions = Transaction.objects.filter(category__user=request.user)
    context = {
        "transactions":transactions,
        "user":request.user,
        }

    return render(request, 'apps/smartmoney/transactions.html', context)

## Displays categories ##
def category(request):
    categories = Category.objects.filter(user = request.user, archived=False)
    context = {"categories":categories}

    return render(request, 'apps/smartmoney/categories.html', context)



#===# Forms #===#
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("vsi:category")
    else:
        form = CategoryForm()
    
    context = {
        "form": form,
        "heading": "Add Category",
        "user":request.user,
        "error_message": "Please correct the errors below" if form.errors else None
    }
    return render(request, "apps/smartmoney/forms.html", context)

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            transaction = form.save(commit=False)
            # Add any additional processing here if needed
            transaction.save()
            return redirect("vsi:transaction")
    else:
        form = TransactionForm(user=request.user)
    
    context = {
        "form": form,
        "heading": "Add Transaction",
        "error_message": "Please correct the errors below" if form.errors else None
    }
    return render(request, "apps/smartmoney/forms.html", context)


def archive_category(request, pk):
    object_to_archive = Category.objects.get(pk=pk)
    object_to_archive.archived = True
    object_to_archive.save()
    
    return redirect("vsi:category")

def delete_transaction(request, pk):
    object_to_delete = Transaction.objects.get(pk=pk)
    object_to_delete.delete()

    return redirect("vsi:transaction")
        

