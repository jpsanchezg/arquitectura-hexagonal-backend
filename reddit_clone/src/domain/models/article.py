from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Article:
    title: str
    content: str
    upvotes: int = field(default=0)
    downvotes: int = field(default=0)
    id: UUID = field(default_factory=uuid4)
