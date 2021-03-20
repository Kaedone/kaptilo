from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(verbose_name="link", max_length=1024)
    delete_after_watching = models.BooleanField(verbose_name="delete")


    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return "{} {} {}".format(self.user, self.header, self.pk)
