from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppMyBlogConfig(AppConfig):
    name = 'app_my_blog'
    verbose_name = _('blog')
