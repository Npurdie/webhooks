from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator

# Create your models here.
class FBUser(models.Model):

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    user_id = models.SlugField(default='', max_length=16, validators=[MinLengthValidator(16)]) #contains only letters, numbers, underscores, or hyphens, usually used in URLs
    user_type = models.CharField(max_length=70, null=True)
    mcgill_email = models.EmailField(default='', max_length=254, validators=[EmailValidator(message="Please enter a valid McGill email address.", whitelist="mcgill.ca")])
    authentication_status = models.CharField(default='authentication_no', max_length=20)
    code = models.SlugField(default='', max_length=20)
    timezone = models.IntegerField(default = -5)

    def __str__(self):
        return ("%s %s" % (self.first_name , self.last_name))

    def set_user_type(self, user_type):
        self.user_type = user_type
        self.save()

class StudentSociety(models.Model):
    fbuser = models.ForeignKey(FBUser, on_delete=models.CASCADE)
    def __str__(self):
        return ("%s" % (self.fbuser.first_name))

class Conversation(models.Model):
    fbuser = models.ForeignKey(FBUser, on_delete=models.CASCADE)
    question = models.PositiveIntegerField()

    def __str__(self):
        return ("%s %s" % (self.fbuser.first_name , self.question))

    def set_conversation_question(self, question):
        self.question = question
        self.save()

class Event(models.Model):
    name = models.CharField(max_length=70, null=True)
    location = models.CharField(max_length=70, null=True)
    description = models.CharField(max_length=300, null=True)
    link = models.CharField(max_length=300, null=True)
    creator = models.ForeignKey(StudentSociety, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    event_time = models.DateField(null=True)

    def __str__(self):
        return ("%s %s %s %s" % (self.name , self.location, self.description, self.creator.fbuser.first_name))
