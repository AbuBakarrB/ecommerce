from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Welcome, {username}!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form":form})
