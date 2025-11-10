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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['category'].queryset = Category.objects.filter(user=user, archived=False)




    
