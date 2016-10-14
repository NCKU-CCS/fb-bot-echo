from django.conf import settings
from django.http import HttpResponse
from django.views import View

class FBWebhook(View):

    def post(self, reqeust, *args, **kwargs):
        return HttpResponse(status=200)

    def get(self, request, *args, **kwargs):
        verification_code = settings.VERIFICATION_CODE
        verify_token = request.GET.get('hub.verify_token', '')
        if verification_code != verify_token:
            return HttpResponse(status=400)

        return HttpResponse(request.GET.get('hub.challenge', ''))

