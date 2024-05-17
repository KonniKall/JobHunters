from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django.forms import fields
from .models import Profile, ContactInfo

# from crispy_forms.helper import FormHelper


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"v-on:change": "isEmail()", "v-model": "email"}),
    )
    # , '@keypress':'isEmail()'

    username = forms.CharField(
        max_length=20,
        help_text="20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(
            attrs={
                "@keypress": "isUser()",
                "v-on:change": "isUser()",
                "v-model": "username",
            }
        ),
    )
    # @keypress="isNumber($event)"

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"v-on:change": "isPassword()", "v-model": "password1"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"v-on:change": "isPassword()", "v-model": "password2"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class UserSignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserSignInForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "field"})
        self.fields["password"].widget.attrs.update({"class": "password_field"})
        # self.fields['username'].label = "Hello"
        # self.fields['password'].label = ""
        # self.helper = FormHelper()
        # self.helper.form_show_labels = False


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_img", "email", "phone_nr"]


class ContactInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["full_name"]
