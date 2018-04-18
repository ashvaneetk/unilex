from django.db import models

from vocabulary.models import Concept


class Record(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=255, blank=True)
    url = models.URLField(unique=True)

    def get_absolute_url(self):
        return "/tag/%s" % self.url

    def __str__(self):
        return self.title


class Tag(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
