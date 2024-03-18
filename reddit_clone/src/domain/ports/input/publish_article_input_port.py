from typing import Protocol
from uuid import UUID

from ...models import Article


class PublishArticleInputPort(Protocol):
    def publish_article(self, article: Article) -> Article:
        raise NotImplementedError()
    
    def get_all_articles(self, article_id: UUID) -> Article:
        raise NotImplementedError()

