from django.db import models


class Websites(models.Model):
    rank = models.PositiveBigIntegerField(db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    url = models.URLField(db_index=True)

    def __str__(self) -> str:
        return self.title