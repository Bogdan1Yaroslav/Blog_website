from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# ----------------------------------------------------------------------------------------------------------------------
# Модель профиля

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("birth date"))
    city = models.CharField(max_length=36, blank=True, verbose_name=_("city"))
    email = models.EmailField(max_length=30, blank=True, verbose_name=_("email"))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True,
                                    verbose_name=_("telephone"))
    number_of_publications = models.PositiveIntegerField(default=0, editable=False,
                                                         verbose_name=_("number of publications"))

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')


# ----------------------------------------------------------------------------------------------------------------------
# Модель поста

class Post(models.Model):
    STATUS_CHOICES = [
        ("a", "active"),
        ("no", "not active")
    ]

    post_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name=_('Post author'))
    post_title = models.CharField(max_length=2000, verbose_name=_("Post title"))
    post_content = models.TextField(verbose_name=_("Content"))
    publication_date = models.DateField(auto_now_add=True, verbose_name=_("Publication date"))
    editing_date = models.DateField(auto_now=True, verbose_name=_("Edit date"))
    is_published = models.BooleanField(default=True, verbose_name=_("Activity status"))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="no", verbose_name=_("Status"))

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ["-publication_date"]
        verbose_name_plural = _('posts')
        verbose_name = _('post')


# ----------------------------------------------------------------------------------------------------------------------
# Модель файла

class Image(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Post name"))
    images = models.FileField(upload_to="files/", verbose_name=_("Path"))

    def __str__(self):
        return str(self.post_id)

    class Meta:
        verbose_name_plural = _('images')
        verbose_name = _('image')
