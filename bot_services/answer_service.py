import re
from bot_services.user_service import UserService, Question
from bot_services.communication_service import CommunicationService
from bot_services.authentication_service import AuthenticationService
from bot_services.event_service import EventService
from bot_services.calendar_service import CalendarService

MSG_ASK_FOR_USER_TYPE = 'Are you a [student] or [instructor]?'
QUESTION_USER_TYPE = 'USER_TYPE'
QUESTION_AUTHENTICATE = 'AUTHENTICATE'
QUESTION_NOTHING = 'NOTHING'

#NLP STUFF
import os.path
import sys
import json
from bot_services.jsonToFunc import sonToFunc

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '8839e93fbba447f0a8b93e6979aefce0'
#NLP STUFF


class AnswerService:
    #TODO:make it more elegant if possible
    def getUsertype(answer):
        searchObj = re.search(r'\b[Ss]tudent\b',answer)
        if searchObj:
            return 'student'
        else:
            searchObj = re.search(r'\b[Ii]nstructor\b',answer)
            if searchObj:
                return 'instructor'
            else:
                return None

    def isCalendar(answer):
        searchObj = re.search(r'\b[Cc]alendar\b',answer)
        if searchObj:
            return True
        return False

    def isPostEvent(answer):
        searchObj = re.search(r'\b[Pp]ost event\b',answer)
        if searchObj:
            return True
        return False

    def isMsgAll(answer):
        searchObj = re.search(r'\b[Mm]sg all\b',answer)
        if searchObj:
            return True
        return False

    # business logic
    def process_message(message):
        # Get user.
        user_id = (message['sender']['id'])
        user_info = CommunicationService.get_user_info(user_id).json()
        fbuser = UserService.getUser(user_id)

        # If user does not exist, create user, create conversation, and ask for user type first.
        if(fbuser is None):
            fbuser = UserService.create_new_user(user_info,user_id)
            conversation = UserService.create_new_conversation(fbuser)
            return "Hi, " + fbuser.first_name + "! " + MSG_ASK_FOR_USER_TYPE

        # If user exist, so must conversation. Get conversation.
        conversation = UserService.get_conversation(fbuser)
        msg = message['message']['text']

        # If the question is user type, check if the user answers with user type
        if(conversation.question == Question.get_question_type(QUESTION_USER_TYPE)):
            fbuser_type = AnswerService.getUsertype(msg)
            # User did not answer with his user type.
            if (fbuser_type is None):
                return MSG_ASK_FOR_USER_TYPE
            else:
                # Record user type.
                fbuser.set_user_type(fbuser_type)
                conversation.set_conversation_question(Question.get_question_type(QUESTION_NOTHING))
                return "Okay, you are a "+ fbuser_type + ". You can now authenticate anytime by typing [authenticate]."

        # If the question type is authentication, check the user's authentication status to do corresponding works.
        elif(conversation.question == Question.get_question_type(QUESTION_AUTHENTICATE)):
            reply = AuthenticationService.authenticationProcess(fbuser, msg)
            if(fbuser.authentication_status == AuthenticationService.AUTHENTICATION_NO):
                conversation.set_conversation_question(Question.get_question_type(QUESTION_NOTHING))
            if(fbuser.authentication_status == AuthenticationService.AUTHENTICATION_DONE):
                conversation.set_conversation_question(Question.get_question_type(QUESTION_NOTHING))
            return reply

        # If it's about event
        elif(Question.about_event(conversation.question)):
            reply = EventService.processEvent(conversation, msg)
            return reply

        # If the question is empty, the msg must be a question.
        elif(conversation.question == Question.get_question_type(QUESTION_NOTHING)):
            if (AnswerService.isPostEvent(msg)):
                ssociety = UserService.get_student_society(fbuser)
                if (ssociety is None):
                    return "Sorry you can't post event because you are not student society"
                reply = EventService.initEvent(conversation)
                return reply
            #if user enteres msg_all, will change when AI recognizes user wants to send mass message
            elif(AnswerService.isMsgAll(msg.split(":")[0])):
                if(UserService.is_admin(fbuser)):
                    if (":" not in msg):
                        return "please enter [msg all:your message]"
                    CommunicationService.post_facebook_message_to_all(msg.split(":")[1])
                    return"Your message has been sent to all registered users"
                return "Only admins can message all users"
            #API.AI STUFF
            ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
            request = ai.text_request()
            request.lang = 'de'  # optional, default value equal 'en'
            request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
            request.query = msg
            response = request.getresponse()
            apiJSON = response.read()
            str_apiJSON = apiJSON.decode('utf-8')
            jsonDict = json.loads(str_apiJSON)
            return sonToFunc(jsonDict["result"], message)

            return "You asked me something, but I don't know how to answer yet."
        return msg
