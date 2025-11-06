from django.shortcuts import render, redirect
from .forms import CategoryForm, TransactionForm
from .models import Category, Transaction

#===# Switch between pages #===#
def dashboard(request):
    return render(request, 'apps/smartmoney/dashboard.html')

def transaction(request):
    transactions = Transaction.objects.all()
    context = {"transactions":transactions}
    

    return render(request, 'apps/smartmoney/transactions.html', context)


def category(request):
    categories = Category.objects.all()
    context = {"categories":categories}

    return render(request, 'apps/smartmoney/categories.html', context)



#===# Forms #===#
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("vsi:category")
    else:
        form = CategoryForm()
        context = {"form":form, "heading":"Add Category"}
    

    return render(request, "apps/smartmoney/forms.html", context)

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("vsi:transaction")
    
    else:
        form = TransactionForm()

        context = {"form": form, "heading":"Add Transaction"}

    return render(request, "apps/smartmoney/forms.html", context)



