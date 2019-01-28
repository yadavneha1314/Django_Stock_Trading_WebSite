from django.conf.urls import *
from Stocks_Trading.stocks_app import views
from django.contrib.auth.views import login

urlpatterns = [
    #url(r'^',include('main.urls')),
    url(r'^login/$',include('Stocks_Trading.stocks_app.login.urls')),
    url(r'^success/$',views.successful_login, name='successful_login' ),
    url(r'^register/$',include('Stocks_Trading.stocks_app.register.urls')),

]
