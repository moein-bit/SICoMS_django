from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()             

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


'''
class ProfileInfoForm(forms.ModelForm):
    MAJORS = (
        ('MED', "Medicine"),
        ('OTH', 'Other'),
    )
    
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
        model = Profile
        fields = ['first_name', 'last_name', 'major', 'semester', 'student_id', 'university']
'''
