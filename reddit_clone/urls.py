from typing import cast

from django.apps import apps
from django.urls import URLPattern, path

from .apps import RedditCloneConfig
from .views import ArticleView

app_config: RedditCloneConfig = cast(
    RedditCloneConfig, apps.get_containing_app_config("reddit_clone")
)

article_view = app_config.dependencies[ArticleView.__name__]

urlpatterns: list[URLPattern] = [
    path("article", article_view),
]
