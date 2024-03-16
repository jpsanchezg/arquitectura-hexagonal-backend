from typing import Any, Dict

from app.aplicacion.adapter.api.http.voto_articulo_view import ArticleVoteView
from app.aplicacion.adapter.api.http.articulo_view import ArticleView

from app.aplicacion.adapter.spi.persistence.repository.voting_user_repository import (
    VotingUserRepository
)
from app.aplicacion.service.rating_articulo_service import ArticleRatingService


def build_production_dependencies_container() -> Dict[str, Any]:
    voting_user_repository = VotingUserRepository()

    article_rating_service = ArticleRatingService(
        find_voting_user_port=voting_user_repository,
        save_voting_user_port=voting_user_repository
    )

    article_vote_django_view = ArticleVoteView.as_view(
        vote_for_article_use_case=article_rating_service
    )
    crearArticulo_view = ArticleView.as_view(
        article_rating_service=article_rating_service
    )

    return {
        'article_vote_django_view': article_vote_django_view
    }
