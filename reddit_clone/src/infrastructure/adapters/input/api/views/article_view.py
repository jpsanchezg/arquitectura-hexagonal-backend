from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ......application.services import ArticleService
from .....mappers import ArticleMapper


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

    def get(self, request: Request) -> Response:
        articles = self.article_service.get_all_articles()

        return Response({"articles": map(ArticleMapper.article_to_json, articles)})
