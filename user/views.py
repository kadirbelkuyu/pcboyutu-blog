from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request, newUser)
            messages.success(request, 'Kayıt işleminiz başarı İle Gerçekleşti. Hoşgeldiniz')
            return redirect("index")
        context = {
            "form": form,
        }

        return render(request, "register.html", context)
    else:
        form = RegisterForm()
        context = {
            "form": form,
        }
        return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Kullanıcı Adı Veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarı ile Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.info(request,"Başarı İle Çıkış Yaptınız")
    return redirect("index")
