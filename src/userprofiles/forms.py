from django import forms


class RegistrationForm(forms.Form):
    # class Meta:
    #     model = SignUp
    #     fields = ['email', 'full_name']
    username  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "Email address", 'type':"email"}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder': "Password", 'type':"password"}))
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder': "Confirm Password", 'type':"password"}))

    def clean(self):

        passw = self.cleaned_data['password']
        cpassw = self.cleaned_data['confirm_password']
        if passw and passw != cpassw:
            raise forms.ValidationError("Passwords don't match")
        # Always return the cleaned data, whether you have changed it or
        #not.
        return self.cleaned_data
