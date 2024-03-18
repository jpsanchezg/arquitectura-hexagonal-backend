from typing import Protocol
from uuid import UUID

from ...models import Article


class ArticleOutputPort(Protocol):
    def save_article(self, article: Article) -> Article:
        raise NotImplementedError()

    def get_all_articles(self) -> list[Article]:
        raise NotImplementedError()

    def get_article_by_id(self, article_id: UUID) -> Article:
        raise NotImplementedError()
