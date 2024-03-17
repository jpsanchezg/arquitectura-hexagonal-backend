from typing import Protocol

from ...models import Article


class ArticleOutputPort(Protocol):
    def save_article(self, article: Article) -> Article:
        raise NotImplementedError()
