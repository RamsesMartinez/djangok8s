import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "djnango_k8s.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import djnango_k8s.users.signals  # noqa: F401, PLC0415
