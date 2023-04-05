from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm,
                                       UserChangeForm as DjangoUserChangeForm)
from captcha.fields import CaptchaField

User = get_user_model()


class CustomUserCreationForm(DjangoUserCreationForm):
    captcha = CaptchaField()

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(DjangoUserChangeForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
