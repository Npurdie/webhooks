from pprint import pprint
from fb_mcbot.models import FBUser, Conversation

class Question:
    question_type = {'NOTHING':0, 'USER_TYPE':1, 'AUTHENTICATE':2}

    def get_question_type(question):
        try:
            result =  Question.question_type.get(question)
        except KeyError:
            pprint("Internal Error! " + question + " is not a question type!")
        return result

class UserService:
    def getUser(userid):
        try:
            user = FBUser.objects.get(user_id = userid)
        except FBUser.DoesNotExist:
            pprint("User id not found in db, the user does not exist.")
            return None
        return user

    def create_new_user(user_info,user_id):
        pprint("Creating new user")
        firstname = user_info['first_name']
        lastname = user_info['last_name']
        timezone = user_info['timezone']
        new_user = FBUser(first_name = firstname, last_name = lastname, user_id =  user_id, timezone = timezone)
        new_user.save()
        return new_user

    def create_new_conversation(fbuser):
        pprint("Creating new conversation")
        new_conversation = Conversation()
        new_conversation.fbuser = fbuser
        #default question USER_TYPE
        new_conversation.question = Question.get_question_type('USER_TYPE')
        new_conversation.save()
        return new_conversation

    def get_conversation(fbuser):
        try:
            conversation = Conversation.objects.get(fbuser = fbuser)
        except Conversation.DoesNotExist:
            pprint("Conversation with " + fbuser.user_id + " not found in db")
            return None
        return conversation
