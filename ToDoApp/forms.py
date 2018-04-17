from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class signup_form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    # Profile_photo = forms.ImageField()

    class Meta(object):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            # 'Profile_photo',
            'password1',
            'password2',
        )

class edit_profile_form(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )
