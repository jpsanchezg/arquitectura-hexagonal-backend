from typing import Protocol

from app.aplicacion.domain.model.vote_for_article_result import VoteForArticleResult
from app.aplicacion.port.api.command.voteForArticleCommand import (
    VoteForArticleCommand
)


class VoteForArticleUseCase(Protocol):
    def vote_for_article(self, command: VoteForArticleCommand) -> VoteForArticleResult:
        raise NotImplementedError()
