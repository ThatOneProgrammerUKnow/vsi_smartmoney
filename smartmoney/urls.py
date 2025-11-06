from django.urls import path
from . import views

app_name = "vsi"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("transactions", views.transaction, name="transaction"),
    path("categories", views.category, name="category"),
    path("add_category", views.add_category, name="add_category"),
    path("add_transaction", views.add_transaction, name="add_transaction"),
]