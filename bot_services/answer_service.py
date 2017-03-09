import re
from bot_services.user_service import UserService, Question
from bot_services.communication_service import CommunicationService
from bot_services.authentication_service import AuthenticationService
from bot_services.calendar_service import CalendarService

MSG_ASK_FOR_USER_TYPE = 'Are you a [student] or [instructor]?'
QUESTION_USER_TYPE = 'USER_TYPE'
QUESTION_AUTHENTICATE = 'AUTHENTICATE'
QUESTION_NOTHING = 'NOTHING'

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

    def isAuthenticate(answer):
        searchObj = re.search(r'\b[Aa]uthenticate\b',answer)
        if searchObj:
            return True
        return False

    def isCalendar(answer):
        searchObj = re.search(r'\b[Cc]alendar\b',answer)
        if searchObj:
            return True
        return False

    def isLogout(answer):
        searchObj = re.search(r'\b[Ll]ogout\b',answer)
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

        # If the question is empty, the msg must be a question.
        elif(conversation.question == Question.get_question_type(QUESTION_NOTHING)):
            # If user enters "authenticate", check if he/she has already been authenticated to do corresponding works.
            #TODO: have a function that check if the answer contains the word 'authenticate'
            if(AnswerService.isAuthenticate(msg)):
                if (fbuser.authentication_status == AuthenticationService.AUTHENTICATION_DONE):
                    return "You have already finished authentication."
                else:
                    conversation.set_conversation_question(Question.get_question_type(QUESTION_AUTHENTICATE))
                return AuthenticationService.authenticationProcess(fbuser, msg)
            # If user enters "logout", reset his/her authentication_status to "authentication_no"
            elif(AnswerService.isLogout(msg)):
                AuthenticationService.resetAuthentication(fbuser)
                conversation.set_conversation_question(Question.get_question_type(QUESTION_NOTHING))
                return "Your are logged out."
            elif(AnswerService.isCalendar(msg)):
                return CalendarService().create_event()

            return "You asked me something, but I don't know how to answer yet."
        return msg
