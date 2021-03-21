from rest_framework.authentication import SessionAuthentication

__all__ = ["CsrfExemptSessionAuthentication"]


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
