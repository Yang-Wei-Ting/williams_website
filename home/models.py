from django.db import models


class HomeCaption(models.Model):
    purpose = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.purpose[:50]
