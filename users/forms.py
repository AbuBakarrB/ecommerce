from django.contrib.auth.forms import UserCreationForm
from django import forms
from commerce.models import CustomUser
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices = CustomUser.USER_TYPE_CHOICES, initial = "buyer")
    class Meta:
        model = get_user_model()
        fields = ('user_type', 'username', 'email', 'password1', 'password2')
