from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def log_in(request):
    errors = []
    next = request.GET.get("next")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_auth = authenticate(username=username, password=password)
        if is_auth:
            login(request, is_auth)
            if next:
                return redirect(next)
            redirect("home:home")
        else:
            error = "Tài khoản hoặc mật khẩu không đúng"
            errors.append(error)
            messages.warning(request, error)

    context = {
        "errors": errors
    }

    return render(request, "log_in/login.html")
