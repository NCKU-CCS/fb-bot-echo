from django.conf.urls import url
from fb import views

urlpatterns = [
    url(r'^$', views.FBWebhook.as_view()),
]
