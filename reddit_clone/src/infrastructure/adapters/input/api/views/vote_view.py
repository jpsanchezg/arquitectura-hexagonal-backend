from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ......application.services import ArticleService
from .....mappers import ArticleMapper, VoteMapper


class VoteView(APIView):
    article_service: ArticleService = None  # type: ignore

    def __init__(self, article_service: ArticleService) -> None:
        self.article_service = article_service
        super().__init__()

    def post(self, request: Request, article_id: str) -> Response:
        article_uuid = UUID(article_id)

        vote_dto = VoteMapper.json_to_dto(request.data)
        article = self.article_service.vote(article_uuid, vote_dto.vote_type)

        return Response({"article": ArticleMapper.article_to_json(article)})
