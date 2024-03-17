from reddit_clone.src.domain.ports.input.publish_article_input_port import (
    PublishArticleInputPort,
)

from ...domain.models import Article
from ...domain.ports.output import ArticleOutputPort


class PublishArticleUseCase(PublishArticleInputPort):
    def __init__(self, article_output_port: ArticleOutputPort):
        self.article_output_port = article_output_port

    def publish_article(self, article: Article) -> Article:
        return self.article_output_port.save_article(article)
