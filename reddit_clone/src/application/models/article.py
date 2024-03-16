from dataclasses import dataclass


@dataclass
class Article:
    title: str
    content: str
    upvotes: int
    downvotes: int
