from django.urls import path
from . import views

app_name = "vsi"

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("categories/", views.category, name="category"),
    path("transactions/", views.transaction, name="transaction"),
    

    # Creating objects
    path("add_category/", views.add_category, name="add_category"),
    path("add_transaction/", views.add_transaction, name="add_transaction"),

    # Deleting objects
    path("category/<int:pk>/archive", views.archive_category, name="archive_category"),
    path("transaction/<int:pk>/delete", views.delete_transaction, name="delete_transaction"),    
]