from typing import Callable

from django.http import HttpResponse

from .src.application.services import ArticleService
from .src.application.usecases import (
    PublishArticleUseCase,
    ReadArticlesUseCase,
    VoteUsecase,
)
from .src.infrastructure.adapters.input.api.views import ArticleView, VoteView
from .src.infrastructure.adapters.output.general_ouput_adapter import (
    GeneralOutputAdapter,
)


def init_dependencies() -> dict[str, Callable[..., HttpResponse]]:
    output_adapter = GeneralOutputAdapter()
    publish_article_use_case = PublishArticleUseCase(output_adapter)
    vote_usecase = VoteUsecase(output_adapter)
    read_articles_usecase = ReadArticlesUseCase(output_adapter)
    article_service = ArticleService(
        publish_article_use_case, read_articles_usecase, vote_usecase
    )
    article_view = ArticleView.as_view(article_service=article_service)
    vote_view = VoteView.as_view(article_service=article_service)

    return {
        ArticleView.__name__: article_view,
        VoteView.__name__: vote_view,
    }
