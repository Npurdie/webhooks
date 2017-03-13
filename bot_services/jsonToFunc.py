# test json input
inTest0 = {
    "action": "walksafe",
    "location": "Lunch with Mary Johnson"
}
inTest1 = {
    "action": "walksafe",
    "location": "Lunch with Mary Johnson",
    "number": "123"
}
inTest2 = {

}
inTest3 = {
    "location": "Lunch with Mary Johnson"
}
inTest4 = {
    "action": "commands",
    "location": "Lunch with Mary Johnson"
}


# import classes for functions here
from bot_services.calendar_service import CalendarService
from bot_services.event_service import EventService

def sonToFunc(inSon):
    if inSon == {}:
        return "Null input"
    if "action" in inSon.keys():
        apiAction = inSon["action"]
        if "parameters" in inSon.keys():
            parameters = inSon["parameters"]
    else:
        return "Invalid input"

    if apiAction == "login":
        return "login"
        # return login()

    elif apiAction == "logout":
        return "logout"
        # return logout()

    elif apiAction == "walksafe":
        if "location" in inSon.keys() and "number" in inSon.keys():
            return ["walksafe", inSon["location"], inSon["number"]]
            # return walksafe(inSon["location"],inSon["number"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "drivesafe":
        if "location" in inSon.keys() and "number" in inSon.keys():
            return ["drivesafe", inSon["location"], inSon["number"]]
            # return drivesafe(inSon["location"],inSon["number"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "rsvp":
        if "event" in inSon.keys() and "status" in inSon.keys():
            return ["rsvp", inSon["event"], inSon["status"]]
            # return rsvp(inSon["event"],inSon["status"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "addEntryCalendar":
        if "name" in parameters.keys() and "date" in parameters.keys() and "time" in parameters.keys() and "description" in parameters.keys():
            name = parameters["name"]
            description = parameters["description"]
            date = parameters["date"]
            time = parameters["time"]
            return CalendarService().create_event_client(name,description)
            # return calenderSet(inSon["event"],inSon["date"],inSon["time"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "events":
        return ["curEvents"]
        # return curEvents()

    elif apiAction == "change":
        if "oldType" in inSon.keys() and "newType" in inSon.keys():
            return ["changeStatus", inSon["oldType"], inSon["newType"]]
            # return changeStatus(inSon["oldType"],inSon["newType"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "minerva":
        if "username" in inSon.keys() and "password" in inSon.keys():
            return ["connectMinerva", inSon["username"], inSon["password"]]
            # return connectMinerva(inSon["username"],inSon["password"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "connect":
        if "calender" in inSon.keys() and "url" in inSon.keys():
            return ["connectCalender", inSon["calender"], inSon["url"]]
            # return connectCalender(inSon["calender"],inSon["url"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "deadlines":
        return EventService().listAllDeadlines()

    elif apiAction == "commands":
        return ["listCommands"]
        # return listCommands()

    elif apiAction == "mac":
        return ["macBus"]
        # return macBus()

    elif apiAction == "broadcast":
        if "class" in inSon.keys() and "message" in inSon.keys():
            return ["broadcast", inSon["class"], inSon["message"]]
            # return broadcast(inSon["class"],inSon["message"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "share":
        if "event" in inSon.keys():
            return ["shareEvent", inSon["event"]]
            # return shareEvent(inSon["event"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "delete":
        if "event" in inSon.keys():
            return ["deleteEvent", inSon["event"]]
            # return deleteEvent(inSon["event"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "status":
        if "event" in inSon.keys():
            return ["statusEvent", inSon["event"]]
            # return statusEvent(inSon["event"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "link":
        if "event" in inSon.keys() and "page" in inSon.keys():
            return ["linkEvent", inSon["event"], inSon["page"]]
            # return linkEvent(inSon["event"],inSon["page"])
        else:
            return "Error: Incomplete Input"

    elif apiAction == "my":
        return ["curStatus"]
        # return curStatus()
    elif apiAction == "sayingHello":
        return "Hi! How may I help you?"
    else:
        return "Invalid input"


print (sonToFunc(inTest0))
print (sonToFunc(inTest1))
print (sonToFunc(inTest2))
print (sonToFunc(inTest3))
print (sonToFunc(inTest4))