from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField("link", max_length=1024)
    permanent = models.BooleanField("permanent")

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return "{} {}".format(self.user, self.pk)
