from django import forms

# from .models import SignUp

class SignUpForm(forms.Form):
    # class Meta:
    #     model = SignUp
    #     fields = ['email', 'full_name']
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "Enter your email address", 'type':"email"}))
    name  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "Enter your name"}))
