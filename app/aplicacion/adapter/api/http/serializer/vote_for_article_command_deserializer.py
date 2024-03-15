from rest_enumfield import EnumField
from rest_framework import serializers

from app.aplicacion.domain.model.voto import Vote
from app.aplicacion.port.api.command.voteForArticleCommand import (
    VoteForArticleCommand
)


class VoteForArticleCommandDeserializer(serializers.Serializer[VoteForArticleCommand]):
    user_id = serializers.UUIDField()
    article_id = serializers.UUIDField()
    vote = EnumField(Vote)

    # Ignored mypy error:
    # Signature of "create" incompatible with supertype "BaseSerializer"
    def create(self) -> VoteForArticleCommand:  # type: ignore
        """
        Create and return a new `VoteForArticleCommand` instance,
        given the validated data.
        """
        return VoteForArticleCommand(**self.validated_data)
