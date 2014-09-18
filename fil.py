#!/usr/bin/python2
# -*- coding: utf-8
#Django settings
from django.core.management import setup_environ
from ask_me import settings
setup_environ(settings)
#Connecting with models
from ask.models import *
from django.contrib.auth.models import User

for i in range(860,10070):
    print i
    r = Rate.objects.get(user_id = i)
    i+=1
