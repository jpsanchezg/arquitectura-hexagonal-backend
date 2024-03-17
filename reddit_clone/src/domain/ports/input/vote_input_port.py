from typing import Protocol
from uuid import UUID

from ...models import Article, VoteType


class VoteInputPort(Protocol):
    def vote(self, article_id: UUID, vote_type: VoteType) -> Article:
        raise NotImplementedError()
