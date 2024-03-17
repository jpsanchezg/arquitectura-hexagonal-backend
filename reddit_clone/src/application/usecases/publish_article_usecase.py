from ...domain.models import Article
from ...domain.ports.output import ArticleOutputPort


class PublishArticleUseCase:
    def __init__(self, article_output_port: ArticleOutputPort):
        self.article_output_port = article_output_port

    def execute(self, article: Article) -> None:
        self.article_output_port.save_article(article)
