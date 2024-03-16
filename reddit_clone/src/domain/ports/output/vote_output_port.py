from typing import Protocol
from uuid import UUID

from ...models import VoteType


class VoteOutputPort(Protocol):
    def vote_article(self, article_id: UUID, vote_type: VoteType) -> None:
        raise NotImplementedError()
