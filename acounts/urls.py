from django.urls import path
from . import views

app_name = "acounts"

urlpatterns = [
    path("", views.sign_up, name="sign_up"),
    path("sign_in", views.sign_in, name="sign_in"),
]