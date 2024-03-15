from typing import Protocol

from app.aplicacion.domain.model.voting_user import VotingUser


class SaveVotingUserPort(Protocol):
    def save_voting_user(self, voting_user: VotingUser) -> VotingUser:
        raise NotImplementedError()
