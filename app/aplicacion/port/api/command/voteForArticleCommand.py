from dataclasses import dataclass

from app.aplicacion.domain.model.identifier.article_id import ArticleId
from app.aplicacion.domain.model.identifier.user_id import UserId
from app.aplicacion.domain.model.voto import Vote


@dataclass
class VoteForArticleCommand:
    article_id: ArticleId
    user_id: UserId
    vote: Vote
