import urllib

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

__all__ = ["Link"]


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField("Link", max_length=1024)
    uses = models.IntegerField("Uses count", default=0)
    shortened = models.URLField("Shortened link", null=True, default=None)
    created = models.DateTimeField("Creation date", auto_now_add=True)

    class Meta:
        app_label = "link"
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def get_shortened_link(self, request):
        url = "http://" + request.get_host() + "/" + str(self.pk)
        url = urllib.parse.quote(url)
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(settings.API_KEY, url))
        data = r.json()
        if data['url']['status'] == 7:
            self.shortened = data['url']['shortLink']
            self.save()
            return True
        return False

    def __str__(self):
        return "{} {}".format(self.user, self.pk)
