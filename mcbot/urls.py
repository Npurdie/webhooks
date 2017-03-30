"""mcbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.management.base import BaseCommand
from bot_mcgill.models import McgillEvent
import json
import _datetime
import pytz
from bot_services.user_service import UserService, Question
from datetime import datetime
from fb_mcbot.models import Event
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fb_mcbot/', include('fb_mcbot.urls')),
]

def one_time_startup():
	Event.objects.filter(event_time__lt=datetime.now()).delete()

one_time_startup()
