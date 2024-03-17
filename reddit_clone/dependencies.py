from typing import Callable

from django.http import HttpResponse

from .src.application.services import ArticleService
from .src.application.usecases import PublishArticleUseCase, VoteUsecase
from .src.infrastructure.adapters.api.views import ArticleView
from .src.infrastructure.adapters.db.repositories import ArticleRepository


def init_dependencies() -> dict[str, Callable[..., HttpResponse]]:
    article_repository = ArticleRepository()
    publish_article_use_case = PublishArticleUseCase(article_repository)
    vote_usecase = VoteUsecase(article_repository)
    article_service = ArticleService(publish_article_use_case, vote_usecase)
    article_view = ArticleView.as_view(article_service=article_service)

    return {ArticleView.__name__: article_view}
