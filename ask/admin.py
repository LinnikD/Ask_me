from django.contrib import admin
from ask.models import *
from django.contrib.auth.models import User

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Rate)
admin.site.register(VoteQuestion)
admin.site.register(VoteAnswer)
