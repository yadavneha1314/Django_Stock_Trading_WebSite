from django.conf.urls import *
from Stocks_Trading.stocks_app.login import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^',login, {'template_name': 'login/login.html'}),
]
