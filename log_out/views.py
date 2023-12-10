from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def log_out(request):
    logout(request)
    return redirect("log_in:log_in")
