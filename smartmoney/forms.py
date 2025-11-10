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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.filter(archived=False)




    
