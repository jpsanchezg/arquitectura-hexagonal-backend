from typing import Protocol
from uuid import UUID

from ...models import Article


class ReadArticlesInputPort(Protocol):
    def get_all_articles(self) -> list[Article]:
        raise NotImplementedError()

    def get_article_by_id(self, article_id: UUID) -> Article:
        raise NotImplementedError()
