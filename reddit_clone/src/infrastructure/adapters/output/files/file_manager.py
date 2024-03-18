import json
import os
from typing import Any
from uuid import UUID

from .....domain.errors import ArticleNotFoundError
from .....domain.models.article import Article
from .....domain.models.vote_type import VoteType
from .....domain.ports.output import ArticleOutputPort, VoteOutputPort
from ....mappers import ArticleMapper


class FileManager(ArticleOutputPort, VoteOutputPort):
    path = "data/files/articulos.json"

    def __init__(self) -> None:
        super().__init__()

    def save_article(self, article: Article) -> Article:
        json = ArticleMapper.article_to_json(article)

        data = self._read_file()
        data["articulos"].append(json)
        self._write_file(data)

        return article

    def get_all_articles(self) -> list[Article]:
        data = self._read_file()

        return [ArticleMapper.json_to_article(el) for el in data["articulos"]]

    def get_article_by_id(self, article_id: UUID) -> Article:
        data = self._read_file()

        for el in data["articulos"]:
            if el["id"] == str(article_id):
                return ArticleMapper.json_to_article(el)

        raise ArticleNotFoundError(article_id)

    def vote_article(self, article_id: UUID, vote_type: VoteType) -> Article:
        data = self._read_file()

        article: Article | None = None

        for el in data["articulos"]:
            if el["id"] == str(article_id):
                if vote_type == VoteType.UPVOTE:
                    el["upvotes"] += 1
                else:
                    el["downvotes"] += 1
                article = ArticleMapper.json_to_article(el)

        if article is None:
            raise ArticleNotFoundError(article_id)

        self._write_file(data)

        return article

    def _read_file(self) -> dict[str, Any]:
        if not os.path.exists(self.path):
            with open(f"{self.path}", "w") as file:
                json.dump({"articulos": []}, file)
            return {"articulos": []}

        with open(f"{self.path}") as file:
            data = file.read()
            if data == "":
                return {"articulos": []}
            return json.loads(data)

    def _write_file(self, data: dict[str, Any]) -> None:
        with open(f"{self.path}", "w") as file:
            json.dump(data, file)
