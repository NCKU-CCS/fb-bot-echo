from django.http import HttpResponse
from django.views import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        html_str = "<html><head><title>Test For Msg</title><body>純粹測試FB bot功能，並不會紀錄任何使用者資訊：）</body></head></html>"
        return HttpResponse(html_str,status=200)
