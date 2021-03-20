import ipinfo
from django.conf import settings

access_token = settings.ACCESS_TOKEN
handler = ipinfo.getHandler(access_token)


def get_ip(ip_address):
    details = handler.getDetails(ip_address)
    return details
