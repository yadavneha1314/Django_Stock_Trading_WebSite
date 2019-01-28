# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Stocks_Trading.stocks_app.forms import * 
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'register/reg_form.html', args)
