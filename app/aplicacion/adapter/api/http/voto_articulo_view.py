from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.aplicacion.adapter.api.http.problem_response import problem_response
from app.aplicacion.adapter.api.http.serializer.resultado_voto_exitoso_serializer import (  # noqa
    SuccessfullyVotedResultSerializer
)
from app.aplicacion.adapter.api.http.serializer.vote_for_article_command_deserializer import (  # noqa
    VoteForArticleCommandDeserializer
)
from app.aplicacion.domain.model.vote_for_article_result import (
    AlreadyVotedResult,
    InsufficientKarmaResult,
    SuccessfullyVotedResult,
    VoteForArticleResult
)
from app.aplicacion.port.api.command.voteForArticleCommand import (
    VoteForArticleCommand
)
from app.aplicacion.port.api.guardar_usuario_voto_port import (
    VoteForArticleUseCase
)
from app.aplicacion.util.assert_never import assert_never


class ArticleVoteView(APIView):
    # default `None` and # `type: ignore` for sake of .as_view()
    # which requires passed attributes to be declared on the class level :(
    vote_for_article_use_case: VoteForArticleUseCase = None  # type: ignore

    def __init__(self, vote_for_article_use_case: VoteForArticleUseCase):
        self.vote_for_article_use_case = vote_for_article_use_case
        super().__init__()

    def post(self, request: Request) -> Response:
        vote_for_article_command = self._read_command(request)
        result = self.vote_for_article_use_case.vote_for_article(
            vote_for_article_command
        )
        return self._build_response(result)

    def _read_command(self, request: Request) -> VoteForArticleCommand:
        serializer = VoteForArticleCommandDeserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.create()

    def _build_response(self, voting_result: VoteForArticleResult) -> Response:
        response = None

        match voting_result:
            case SuccessfullyVotedResult():
                response_data = SuccessfullyVotedResultSerializer(
                    voting_result).data
                response = Response(response_data, status=HTTPStatus.CREATED)
            case InsufficientKarmaResult():
                response = problem_response(
                    title="Cannot vote for an article",
                    detail=voting_result.to_message(),
                    status=HTTPStatus.BAD_REQUEST
                )
            case AlreadyVotedResult():
                response = problem_response(
                    title="Cannot vote for an article",
                    detail=voting_result.to_message(),
                    status=HTTPStatus.CONFLICT
                )
            case _:
                assert_never(voting_result)
        return response
