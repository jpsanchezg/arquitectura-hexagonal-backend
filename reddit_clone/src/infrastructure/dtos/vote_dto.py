from dataclasses import dataclass
from uuid import UUID

from ...domain.models import VoteType


@dataclass
class VoteDTO:
    article_id: UUID
    vote_type: VoteType
