from typing import Protocol

from ...models import Article


class PublishArticleInputPort(Protocol):
    def publish_article(self, article: Article) -> None:
        raise NotImplementedError()