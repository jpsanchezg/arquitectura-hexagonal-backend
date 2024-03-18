import logging
from http import HTTPStatus
from typing import Any

from rest_framework.response import Response
from rest_framework.views import exception_handler

from ...domain.errors import ArticleNotFoundError, FormatError


def problem_response(title: str, detail: str, status: HTTPStatus) -> Response:
    problem_data = {"title": title, "detail": detail, "status": status.value}
    return Response(
        problem_data, status=status.value, content_type="application/problem+json"
    )


logger = logging.getLogger(__name__)


def exceptions_handler(exc: Exception, context: Any):
    logger.error("Unexpected error occurred: %s", exc)

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # NOTE: this is not formatted as Problem response,
    #       currently left as-is for cleaner demo code.
    response = exception_handler(exc, context)
    if response is not None:
        return response

    if isinstance(exc, ArticleNotFoundError):
        return problem_response(
            "Article not found",
            f"Article with id {exc.article_id} does not exist",
            HTTPStatus.NOT_FOUND,
        )

    if isinstance(exc, FormatError):
        return problem_response(
            "Invalid format",
            str(exc),
            HTTPStatus.BAD_REQUEST,
        )

    logger.exception("Unhandled error: %s", exc, exc_info=True)
    return problem_response(
        "Unknown error",
        "Our deepest apologies, an unexpected error occurred "
        "and we are already working on it.",
        HTTPStatus.INTERNAL_SERVER_ERROR,
    )
