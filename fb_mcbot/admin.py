from django.contrib import admin
from fb_mcbot.models import FBUser, Conversation, StudentSociety, Event, Major

# Register your models here.
admin.site.register(FBUser)
admin.site.register(Conversation)
admin.site.register(StudentSociety)
admin.site.register(Event)
admin.site.register(Major)