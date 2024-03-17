from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .....application.services import ArticleService


class ArticleView(APIView):
    article_service: ArticleService = None  # type: ignore

    def __init__(self, article_service: ArticleService) -> None:
        self.article_service = article_service
        super().__init__()

    def post(self, request: Request) -> Response:
        print(request.data)
        return Response()
