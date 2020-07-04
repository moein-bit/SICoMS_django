from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
###
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

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

            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'SICoMS account confirmation'
            message = render_to_string('users/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, f"Dear {user.profile.first_name}, Your account has been created!")
            return redirect('email-confirmation')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form,
                                                   'title': 'Registeration'})

def email_confirmation(request):
    return render(request,
                  'users/email_confiramtion.html',
                  context={'title': "Email Confirmation"})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        messages.success(request, "Your account is activated! Welcome to SICoMS!")
        return redirect('homepage-home')
    else:
        messages.error(request, "Something went wrong!")
        return render(request,
                      'users/activation_failed.html',
                      context={"title": "Activation Failed"})



@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form': u_form,
                                                  'p_form': p_form,
                                                  'title': 'Profile'})