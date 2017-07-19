# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
#class HomeView(TemplateView):

#    template_name = 'index.html'


from Website.forms import ContactForm

# add to your views
def contact(request):
    form_class = ContactForm
    
    return render(request, 'index.html', {
        'form': form_class,
    })
