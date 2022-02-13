from django import forms 
from .models import Userbase

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label="Enter Username",min_length=4,max_length=50,help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required':"Sorry, you will need an email"})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = Userbase
        fields = ('user_name', 'email')

    
    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = Userbase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("username already exists")
        return user_name
    
    def clean_password2(self):
        cd = self.changed_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Posswords do not match')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Userbase.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another email, that is already taken')
        return email