from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_my_blog.models import Post, Profile, Image
from django.utils.translation import gettext_lazy as _

# ----------------------------------------------------------------------------------------------------------------------
# Форма аутентификации

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# ----------------------------------------------------------------------------------------------------------------------
# Форма регистрации

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=True, help_text=_("example: 1990-10-10"))
    city = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(required=True, help_text=_("example: +0000000000"))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


# ----------------------------------------------------------------------------------------------------------------------
# Форма юзера

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


# ----------------------------------------------------------------------------------------------------------------------
# Форма профиля

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, input_formats=['%Y-%m-%d'])

    class Meta:
        model = Profile
        fields = ("date_of_birth", "city", "email", "phone_number")


# ----------------------------------------------------------------------------------------------------------------------
# Форма поста

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_author", "post_title", "post_content"]
        widgets = {'post_author': forms.HiddenInput()}


# ----------------------------------------------------------------------------------------------------------------------
# Форма для загрузки нескольких изображений

class MultipleFilesLoadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["images"]
        widgets = {'images': forms.ClearableFileInput(attrs={"multiple": True})}


# ----------------------------------------------------------------------------------------------------------------------
# Форма загрузки постов через csv файл

class UploadPostForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))

# ----------------------------------------------------------------------------------------------------------------------
