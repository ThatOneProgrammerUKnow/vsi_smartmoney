from django.forms import ModelForm
from .models import Category, Transaction


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category"]

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "category", "description", "amount", "type"]




    
