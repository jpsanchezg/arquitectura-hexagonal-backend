from dataclasses import dataclass

from ...domain.models import VoteType


@dataclass
class VoteDTO:
    vote_type: VoteType
