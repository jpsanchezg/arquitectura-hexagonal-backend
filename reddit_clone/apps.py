from typing import Callable

from django.apps import AppConfig
from django.http import HttpResponse


class RedditCloneConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reddit_clone"
    dependencies: dict[str, Callable[..., HttpResponse]]

    def ready(self):
        from .dependencies import init_dependencies

        self.dependencies = init_dependencies()
