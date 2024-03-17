from uuid import UUID

from ....domain.models import Article, VoteType
from ....domain.ports.output import ArticleOutputPort, VoteOutputPort
from .db.repositories import ArticleRepository
from .files import FileManager


class GeneralOutputAdapter(ArticleOutputPort, VoteOutputPort):
    def __init__(self) -> None:
        self.article_repository = ArticleRepository()
        self.file_manager = FileManager()
        super().__init__()

    def save_article(self, article: Article) -> Article:
        self.file_manager.save_article(article)
        return self.article_repository.save_article(article)

    def vote_article(self, article_id: UUID, vote_type: VoteType) -> Article:
        self.file_manager.vote_article(article_id, vote_type)
        return self.article_repository.vote_article(article_id, vote_type)
