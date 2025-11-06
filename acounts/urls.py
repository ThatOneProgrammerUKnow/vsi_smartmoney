from django.urls import path
from . import views

app_name = "acounts"

urlpatterns = [
    path("", views.index, name="index")
]