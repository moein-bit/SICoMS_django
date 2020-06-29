from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    MAJORS = (
        ('MED', "Medicine"),
        ('OTH', 'Other'),
    )
    email = forms.EmailField()             
    first_name = forms.CharField(max_length=50, 
                                 required=True, 
                                 label="First Name")

    last_name = forms.CharField(max_length=50, 
                                required=True,
                                label="Last Name")

    major = forms.ChoiceField(choices=MAJORS, 
                              label="Your Major",
                              required=True)

    semester = forms.IntegerField(label="Semester",
                                  required=True)

    student_id = forms.IntegerField(required=True,
                                    label="Student ID")

    university = forms.CharField(max_length=60,
                                 label="University",
                                 required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'major', 'semester', 
                  'student_id', 'university', 
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'semester', 'university', 'student_id', 'major']