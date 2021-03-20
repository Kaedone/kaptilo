import urllib

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField("Link", max_length=1024)
    permanent = models.BooleanField("Is permanent", default=False)
    uses = models.IntegerField("Uses count", default=0)
    shortened = models.URLField("Shortened link", null=True, default=None)
    created = models.DateTimeField("Creation date", auto_now_add=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def get_shortened_link(self, request):
        url = request.get_host() + "/" + str(self.pk)
        url = urllib.parse.quote(url)
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(settings.API_KEY, url))
        print(r)

    def __str__(self):
        return "{} {}".format(self.user, self.pk)
