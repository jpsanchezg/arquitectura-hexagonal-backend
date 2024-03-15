from app.aplicacion.domain.model.voto_x_articulo import (
    SuccessfullyVotedResult, VoteForArticleResult
)
from app.aplicacion.port.api.command.voteForArticleCommand import (
    VoteForArticleCommand
)
from app.aplicacion.port.api.guardar_usuario_voto_port import (
    VoteForArticleUseCase
)
from app.aplicacion.port.spi.find_voting_user_port import FindVotingUserPort
from app.aplicacion.port.spi.save_voting_user_port import SaveVotingUserPort
from app.aplicacion.util.transactional import transactional


class ArticleRatingService(
    VoteForArticleUseCase
):
    _find_voting_user_port: FindVotingUserPort
    _save_voting_user_port: SaveVotingUserPort

    def __init__(
        self,
        find_voting_user_port: FindVotingUserPort,
        save_voting_user_port: SaveVotingUserPort
    ):
        self._find_voting_user_port = find_voting_user_port
        self._save_voting_user_port = save_voting_user_port

    @transactional
    def vote_for_article(self, command: VoteForArticleCommand) -> VoteForArticleResult:
        voting_user = self._find_voting_user_port.find_voting_user(
            command.article_id,
            command.user_id
        )

        voting_result = voting_user.vote_for_article(
            command.article_id,
            command.vote
        )

        match voting_result:
            case SuccessfullyVotedResult():
                self._save_voting_user_port.save_voting_user(voting_user)

        return voting_result
