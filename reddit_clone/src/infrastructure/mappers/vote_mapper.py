from typing import Any

from ...domain.errors import FormatError
from ...domain.models import VoteType
from ..dtos import VoteDTO


class VoteMapper:
    @staticmethod
    def json_to_dto(json: Any) -> VoteDTO:
        try:
            return VoteDTO(vote_type=VoteType(json["vote_type"]))
        except (KeyError, ValueError):
            raise FormatError("vote_type")
