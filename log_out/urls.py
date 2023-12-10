from django.urls import path
from . import views

app_name = "log_out"

urlpatterns = [
    path('', views.log_out, name="log_out"),
]
