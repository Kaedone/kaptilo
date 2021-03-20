from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="text")
    delete_after_watching = models.BooleanField(verbose_name="delete")
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
