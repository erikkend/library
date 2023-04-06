from django import forms

from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm,
                                       UserChangeForm as DjangoUserChangeForm)
from captcha.fields import CaptchaField
from django.forms import TextInput, EmailInput

User = get_user_model()


class CustomUserCreationForm(DjangoUserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control h6"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control h6"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    captcha = CaptchaField()

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control h6l",
            }),
            'email': EmailInput(attrs={
                'class': "form-control h6",
            })
        }


class CustomUserChangeForm(DjangoUserChangeForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
