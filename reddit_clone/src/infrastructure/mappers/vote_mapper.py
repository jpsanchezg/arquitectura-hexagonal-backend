from typing import Any

from ...domain.models import VoteType
from ..dtos import VoteDTO


class VoteMapper:
    @staticmethod
    def json_to_dto(json: Any) -> VoteDTO:
        return VoteDTO(vote_type=VoteType(json["vote_type"]))
