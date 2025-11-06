from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('E', 'Expences'),
        ('I', 'Income')
    ]
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)

    def __str__(self):
        if self.type == "I":
            return f"R {self.amount} went to {self.category} on {self.date.day}/{self.date.month}/{self.date.year}."
        else:
            return f"R {self.amount} came from {self.category} on {self.date.day}/{self.date.month}/{self.date.year}"
