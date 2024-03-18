from uuid import UUID

from ...domain.models import Article
from ...domain.ports.input import ReadArticlesInputPort
from ...domain.ports.output import ArticleOutputPort


class ReadArticlesUseCase(ReadArticlesInputPort):
    def __init__(self, article_output_port: ArticleOutputPort):
        self.article_output_port = article_output_port

    def get_all_articles(self) -> list[Article]:
        return self.article_output_port.get_all_articles()

    def get_article_by_id(self, article_id: UUID) -> Article:
        return self.article_output_port.get_article_by_id(article_id)
