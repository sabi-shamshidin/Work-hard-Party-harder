from django.db import models


class Result(models.Model):
    path = models.CharField(max_length=100, null=False, blank=False)
    prediction = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.path
