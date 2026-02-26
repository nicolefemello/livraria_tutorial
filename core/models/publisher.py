from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name