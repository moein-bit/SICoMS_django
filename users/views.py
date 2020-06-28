from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm#, ProfileInfoForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        #profile_form = ProfileInfoForm(request.POST)
        if form.is_valid():
            form.save()
            #profile_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! Log in by your username: {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
        #profile_form = ProfileInfoForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')