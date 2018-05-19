from django.db import models


class Grid(models.Model):
    x = models.IntegerField(blank=False, null=False)
    y = models.IntegerField(blank=False, null=False)
    data = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
