from django.urls import path
from . import views

app_name = "log_in"

urlpatterns = [
    path('', views.log_in, name="log_in"),
]