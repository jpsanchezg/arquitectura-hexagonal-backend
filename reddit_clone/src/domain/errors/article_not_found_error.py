from uuid import UUID


class ArticleNotFoundError(Exception):
    def __init__(self, article_id: UUID) -> None:
        self.article_id = article_id
        super().__init__(f"Article with id '{article_id}' not found")
