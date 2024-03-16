from dataclasses import dataclass

from .vote_type import VoteType


@dataclass
class Vote:
    id: int
    user_id: int
    post_id: int
    type: VoteType
