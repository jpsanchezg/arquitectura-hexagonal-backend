from typing import Protocol

from app.aplicacion.domain.model.identifier.article_id import ArticleId
from app.aplicacion.domain.model.identifier.user_id import UserId
from app.aplicacion.domain.model.voting_user import VotingUser


class FindVotingUserPort(Protocol):
    def find_voting_user(self, article_id: ArticleId, user_id: UserId) -> VotingUser:
        raise NotImplementedError()
