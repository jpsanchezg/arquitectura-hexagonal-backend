from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .....application.services import ArticleService
from ....mappers import ArticleMapper, VoteMapper


class ArticleView(APIView):
    article_service: ArticleService = None  # type: ignore

    def __init__(self, article_service: ArticleService) -> None:
        self.article_service = article_service
        super().__init__()

    def post(self, request: Request) -> Response:

        article = self.article_service.publish_article(
            ArticleMapper.json_to_article(request.data)
        )

        return Response({"article": ArticleMapper.article_to_json(article)})

    def put(self, request: Request) -> Response:
        vote_dto = VoteMapper.json_to_dto(request.data)
        article = self.article_service.vote(vote_dto.article_id, vote_dto.vote_type)

        return Response({"article": ArticleMapper.article_to_json(article)})
