from uuid import UUID

from ......domain.models.article import Article
from ......domain.models.vote_type import VoteType
from ......domain.ports.output import ArticleOutputPort, VoteOutputPort
from .....mappers import ArticleMapper
from ..entities import ArticleEntity


class ArticleRepository(ArticleOutputPort, VoteOutputPort):
    def __init__(self) -> None:
        super().__init__()

    def save_article(self, article: Article) -> Article:
        article_entity = ArticleEntity.objects.create(
            article_id=article.id,
            title=article.title,
            content=article.content,
            upvotes=article.upvotes,
            downvotes=article.downvotes,
        )
        return ArticleMapper.entity_to_article(article_entity)

    def vote_article(self, article_id: UUID, vote_type: VoteType) -> Article:
        article = ArticleEntity.objects.get(article_id=article_id)
        if vote_type == VoteType.UPVOTE:
            article.upvotes += 1
        else:
            article.downvotes += 1
        article.save()

        return ArticleMapper.entity_to_article(article)

    def get_all_articles(self) -> list[Article]:
        return list(map(ArticleMapper.entity_to_article, ArticleEntity.objects.all()))

    def get_article_by_id(self, article_id: UUID) -> Article:
        return ArticleMapper.entity_to_article(
            ArticleEntity.objects.get(article_id=article_id)
        )
