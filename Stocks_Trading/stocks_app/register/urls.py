from django.conf.urls import *
from Stocks_Trading.stocks_app.register import views
from django.contrib.auth.views import login

urlpatterns = [
    url('',views.register, name='register'),
]
