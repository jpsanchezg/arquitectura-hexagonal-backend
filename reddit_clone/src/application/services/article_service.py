from uuid import UUID

from ...domain.models import Article, VoteType
from ...domain.ports.input import PublishArticleInputPort, VoteInputPort


class ArticleService(VoteInputPort, PublishArticleInputPort):
    def __init__(
        self,
        publish_article_input_port: PublishArticleInputPort,
        vote_input_port: VoteInputPort,
    ) -> None:
        self.publish_article_input_port = publish_article_input_port
        self.vote_input_port = vote_input_port

    def vote(self, article_id: UUID, vote_type: VoteType) -> None:
        self.vote_input_port.vote(article_id, vote_type)

    def publish_article(self, article: Article) -> None:
        self.publish_article_input_port.publish_article(article)
