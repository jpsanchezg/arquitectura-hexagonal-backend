from typing import Any
from uuid import UUID

from ...domain.models import VoteType
from ..dtos import VoteDTO


class VoteMapper:
    @staticmethod
    def json_to_dto(json: Any) -> VoteDTO:
        return VoteDTO(
            article_id=UUID(json["article_id"]),
            vote_type=VoteType(json["vote_type"]),
        )
