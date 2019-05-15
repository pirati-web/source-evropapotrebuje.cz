# -*- encoding: utf-8 -*-

import time
from datetime import date, datetime       # timeSlices

import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, resolve_url
from django.template import Template, RequestContext, loader
from django.shortcuts import render
from django.urls import reverse  
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext, pgettext_lazy

import logging

from django.conf import settings as appSettings

# Logger instance
logger = logging.getLogger(__name__)


def about(request):
    template = 'about.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_index(request):
    template = 'page_index.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_index_ar(request):
    template = 'page_index.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_program(request):
    template = 'page_program.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)
def page_program_eu(request, part="preambule"):
    template = 'page_program_eu.html'
    context = {
        'lang' : 'cs',
        'part' : part,
        }

    return render(request, template, context)

def page_jak_volit(request):
    template = 'page_jak_volit.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_kandidati(request):
    template = 'page_kandidati.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_nalodeni(request):
    template = 'page_nalodeni.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_zapoj_se(request):
    template = 'page_zapoj_se.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_proc_jit_volit(request):
    template = 'page_proc_jit_volit.html'
    context = {
        'lang' : 'cs',
        }

    return render(request, template, context)

def page_kandidati_detail(request, person):
    template = 'page_kandidati_detail.html'
    context = {
        'lang' : 'cs',
        'person' : person,
        'person_text' : 'kandidati_detail/%s.html' % (person,),
        }

    return render(request, template, context)


def page_en_what_we_want(request ):
    template = 'page_en_what_we_want.html'
    context = {
        'lang' : 'en',
        }

    return render(request, template, context)

def page_en_how_to_vote(request ):
    template = 'page_en_how_to_vote.html'
    context = {
        'lang' : 'en',
        }

    return render(request, template, context)

def page_sk_jak_volit(request ):
    template = 'page_sk_jak_volit.html'
    context = {
        'lang' : 'sk',
        }

    return render(request, template, context)



