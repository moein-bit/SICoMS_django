from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm#, ProfileInfoForm
from django.contrib.auth import login, authenticate

'''def register(request):
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
    return render(request, 'users/register.html', {'form': form})'''

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.major = form.cleaned_data.get('major')
            user.profile.semester = form.cleaned_data.get('semester')
            user.profile.university = form.cleaned_data.get('university')
            user.profile.student_id = form.cleaned_data.get('student_id')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password, email=email)
            messages.success(request, f"Dear {user.profile.first_name}, Your account has been created! Log in by your username: {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')