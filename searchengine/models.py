from django.db import models


class Websites(models.Model):
    rank = models.PositiveBigIntegerField()
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self) -> str:
        return self.title
