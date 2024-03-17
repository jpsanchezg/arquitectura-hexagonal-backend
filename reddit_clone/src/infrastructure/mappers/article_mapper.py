from typing import Any

from ...domain.models import Article
from ...infrastructure.adapters.output.db.entities import ArticleEntity


class ArticleMapper:
    @staticmethod
    def json_to_article(json: Any) -> Article:
        try:
            return Article(
                title=json["title"],
                content=json["content"],
            )
        except KeyError as e:
            raise ValueError(f"Invalid article: {e}")

    @staticmethod
    def article_to_json(article: Article) -> Any:
        return {
            "id": str(article.id),
            "title": article.title,
            "content": article.content,
            "upvotes": article.upvotes,
            "downvotes": article.downvotes,
        }

    @staticmethod
    def entity_to_article(article_entity: ArticleEntity):
        return Article(
            title=article_entity.title,
            content=article_entity.content,
            upvotes=article_entity.upvotes,
            downvotes=article_entity.downvotes,
            id=article_entity.article_id,
        )
