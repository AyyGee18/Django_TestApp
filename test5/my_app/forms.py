from django import forms
from django.contrib.auth.models import User
from my_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        all_cleaned_data = super().clean()
        pswd = all_cleaned_data["password"]
        conf = all_cleaned_data["confirm_password"]

        if pswd != conf:
            raise forms.ValidationError('Password do not match!')

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
