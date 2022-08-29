


from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Admin
        fields = ["username", "password", "email", "full_name"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "User with this username already exists.")
        return uname


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class SpecialForm(ModelForm):
    class Meta:
        model = Special
        fields = '__all__'
    
class ExclusiveForm(ModelForm):
    class Meta:
        model = Exclusive
        fields = '__all__'