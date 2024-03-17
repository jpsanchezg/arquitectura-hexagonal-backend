from rest_framework.views import APIView

from reddit_clone.src.application.services import ArticleService


class ArticleView(APIView):
    def __init__(self, article_service: ArticleService) -> None:
        self.article_service = article_service
        super().__init__()
