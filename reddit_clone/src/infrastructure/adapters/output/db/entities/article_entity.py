from uuid import uuid4

from django.db import models


class ArticleEntity(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    class Meta:
        # in a real application this could be a view or a table intended for reads only
        # (i.e. think of CQRS).
        db_table = "articulos"
