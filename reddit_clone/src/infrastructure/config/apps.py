from django.apps import AppConfig
from rest_framework.views import APIView


class RedditCloneConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reddit_clone"
    dependencies: dict[str, APIView]

    def ready(self):
        from .dependencies import init_dependencies

        self.dependencies = init_dependencies()
