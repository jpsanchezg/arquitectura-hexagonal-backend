from typing import cast

from django.apps import apps as django_apps
from django.urls import path

from app.apps import MyAppConfig

app_config: MyAppConfig = cast(
    MyAppConfig,
    django_apps.get_containing_app_config('app')
)
article_vote_django_view = app_config.container['article_vote_django_view']
crearArticulo = app_config.container['crearArticulo_view']


urlpatterns = [
    path('votoArticulo', article_vote_django_view),
    path('crearArticulo', article_vote_django_view),
    path('traerArticulo', article_vote_django_view),
    path('crearUsuarios', article_vote_django_view),
]
