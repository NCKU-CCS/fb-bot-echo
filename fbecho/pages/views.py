from django.http import HttpResponse
from django.views import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("純粹測試FB bot功能，並不會紀錄任何使用者資訊：）",status=200)
