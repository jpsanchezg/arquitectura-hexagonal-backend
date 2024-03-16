from dataclasses import dataclass


@dataclass
class ArticleEntity:
    title: str
    content: str
    upvotes: int
    downvotes: int
