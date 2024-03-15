from app.aplicacion.adapter.spi.persistence.entity.voto_articulo_entity import (
    ArticleVoteEntity
)
from app.aplicacion.adapter.spi.persistence.entity.UsuarioVotante_entity import (
    VotingUserEntity
)

# A way to explicitly tell linters that the imported classes are used
__all__ = [
    'ArticleVoteEntity',
    'VotingUserEntity'
]
