from uuid import UUID

from ...domain.models import VoteType
from ...domain.ports.input import VoteInputPort
from ...domain.ports.output import VoteOutputPort


class VoteUsecase(VoteInputPort):
    def __init__(self, vote_output_port: VoteOutputPort):
        self.vote_output_port = vote_output_port

    def vote(self, article_id: UUID, vote_type: VoteType) -> None:
        self.vote_output_port.vote_article(article_id, vote_type)
