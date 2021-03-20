from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="text")
    delete_after_watching = models.BooleanField(verbose_name="delete")
    header = models.CharField(max_length=256, verbose_name='header', default='UNNAMED')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return "{} {} {}".format(self.user, self.header, self.pk)
