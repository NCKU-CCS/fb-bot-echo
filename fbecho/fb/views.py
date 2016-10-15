import json
import requests
from pprint import pprint

from django.conf import settings
from django.http import HttpResponse
from django.views import View

class FBWebhook(View):

    def post(self, request, *args, **kwargs):
        msg_entries = json.loads(request.body.decode('utf-8'))
        pprint (msg_entries)
        post_msg_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={token}'.format(token=settings.FB_TOKEN)
        for entry in msg_entries['entry']:
            for message in entry['messaging']:
                if message.get('message', '') == '':
                    continue
                res_msg = json.dumps({"recipient": message['sender'],
                                      "message": {
                                          "text": message['message']['text']
                                      }})
                print (res_msg)
                req = requests.post(post_msg_url,
                                    headers={"Content-Type": "application/json"},
                                    data=res_msg)
                pprint (req.json())
        return HttpResponse(status=200)

    def get(self, request, *args, **kwargs):
        verification_code = settings.VERIFICATION_CODE
        verify_token = request.GET.get('hub.verify_token', '')
        if verification_code != verify_token:
            return HttpResponse(status=400)

        return HttpResponse(request.GET.get('hub.challenge', ''), status=200)

