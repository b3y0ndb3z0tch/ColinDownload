from datetime import datetime, timedelta
import calendar
import json
# # get current datetime
# dt = datetime.now()
# future_date = dt + timedelta(days=1)
# print('Datetime is:', dt)
# print(future_date)
# print (future_date.strftime('%A'))
# d = future_date.strftime("%x")
# print("Output 2:", d)

from TestingIndividualLogicCode.alerts import email_alert
# list_of_regulars_emails2 used for testing
# NEEDS TO BE REPLACED WITH list_of_regulars_emails WHICH IS NEW INVITED PLAYERS EMAILS

def check_event_already_created(all_events, new_event):
    print("^^^ check_event_already_created ^^^")
    new_event_title = new_event['Location'] + " " + new_event['Time'] + " " + new_event['Date']
    print(new_event_title)
    print(all_events)
    for event in all_events:
        print(event)
        if event != "TotalEventCount":
            created_event_title = all_events[event].get('Location') + " " + all_events[event].get("Time") + " " + all_events[event].get("Date")
            print(created_event_title)
            print(created_event_title)
            if created_event_title == new_event_title:
                print("THIS EVENT IS ALREADY CREATED")
                return True
            else:
                print("We need to create the event")


def check_if_event_already_made(title_of_new_event):
    print("*** check_if_event_already_made function ***")
    with open('C:\ArizoneChadAPP\myevents.json') as allcurrentevents:
        all_current_events = json.load(allcurrentevents)
        print("****   IN THE check_if_event_already_made MODULE   ***")
        print(type(title_of_new_event))
        print(title_of_new_event)
        for key, val in all_current_events.items():
            print(key,val)
            if isinstance(val, dict):
                print("yes the value of the key is a dictionary")
                already_created_event_title = str(val["Date"] + " " + val["Location"] + " " + val["Time"])
                print(already_created_event_title)
                print("^"*100)
                if already_created_event_title == title_of_new_event:
                    print("()()()"*50)
                    print("EVENT ALREADY CREATED")
                    return False
    print("1"*100)
    return True

def check_player_info_for_regular(future_day, val):
    print("***   IN THE check_player_info_for_regular MODULE RETURNS val AND list_of_regulars_emails   ***")
    key = str(val["Location"] + " " + val["Time"])
    with open('C:\ArizoneChadAPP\ContactInfo.json') as listofplayers:
        list_of_all_players = json.load(listofplayers)
        list_of_regulars_emails = []
        for player in list_of_all_players:
            if player.get(key) == "R":
                print("YES THE PLAYER IS A REGULAR")
                val["PlayersInvited"].append(player.get("playerid"))
                list_of_regulars_emails.append(player.get("Email"))
    return val, list_of_regulars_emails
    #need to append the player number into invited
    #myevents.json - event# - {"PlayersInvited"}:[LIST]

def create_future_date_and_future_day(a):
    print("%%% IN THE create_future_date_and_future_day MODULE RETURN future_day AND future_date")
    dt = datetime.now()
    future_date = dt + timedelta(days=a)
    future_day = future_date.strftime('%A')
    future_date = future_date.strftime("%x")
    print(future_date, future_day)
    return str(future_date), str(future_day)

def send_new_automated_event_regular_email(val, list_of_regulars_emails, future_date):
    print("in the send_new_automated_event_regular_email function")
    print(future_date)
    print(type(future_date))
    with open("C:\ArizoneChadAPP\standardmessages.json") as file:
        all_messages = json.load(file)
        email_message = all_messages[val]
        email_message = email_message.replace("insert_date", str(future_date["Date"]))
        email_message = email_message.replace("insert_day", str(future_date["Day"]))
        email_by_date = str(regular_email_date_insert_day(future_date["Day"]))
        email_message = email_message.replace("insert_email_by_date", email_by_date)
        email_message = email_message.replace("insert_time", str(future_date["Time"]))
        email_message = email_message.replace("insert_location", str(future_date["Location"]))
        for player in list_of_regulars_emails:
            email_alert(player, "Test Email", email_message)


def regular_email_date_insert_day(day):
    print("---   in the regular_email_date_insert_day Module   --- called by replace_email_message MODULE")
    email_by_day = "No_Day_Yet"
    dt = datetime.now()
    # print(dt)
    # print(type(dt))
    for a in range(1,8):
        future_day = dt + timedelta(days=a)
        future_day_day = future_day.strftime('%A').upper()
        # print(future_day)
        # print(type(future_day))
        if future_day_day == day:
            future_day_number = future_day.strftime("%w")
            # print(future_day_number)
            # print(type(future_day_number))
            if future_day_number == "0":
                return "Friday"
            elif future_day_number == "1":
                return "Saturday"
            elif future_day_number == "2":
                return "Sunday"
            elif future_day_number == "3":
                return "Monday"
            elif future_day_number == "4":
                return "Tuesday"
            elif future_day_number == "5":
                return "Wednesday"
            elif future_day_number == "6":
                return "Thursday"


def check_current_day_for_new_event():
    print("in the check_current_day_for_new_event function")
    for a in range(1,7):
        future_date, future_day = create_future_date_and_future_day(a)
        with open("C:\ArizoneChadAPP\quickevents.json") as f:
            quick_events = json.load(f)
            print(quick_events)
            for key, val in quick_events.items():
                print(key,val)
                if isinstance(val, dict):
                    print("YES ITS A DICT")
                    print(val.items())
                    for key2, val2 in val.items():
                        print(key2, val2)
                        print("^"*100)
                        print(future_day.upper())
                        print(type(future_day))
                        if str(key2) == "Day" and val2 == future_day.upper():
                            print("%%% JUST CHECKED QUICK EVENT DAY TO FUTURE DAY &&&")
                            print(key)
                            print(val)
                            title_of_new_event = str(future_date) + " " + val.get("Location") + " " + val.get("Time")
                            print(title_of_new_event)
                            print("^"*100)
                            if check_if_event_already_made(title_of_new_event):
                                with open('C:\ArizoneChadAPP\myevents.json') as allcurrentevents:
                                    print("999"*50)
                                    print("we've made it into here")
                                    all_current_events = json.load(allcurrentevents)
                                    new_event_id = 1 + all_current_events['TotalEventCount']
                                    all_current_events['TotalEventCount'] = new_event_id
                                    print(type(new_event_id))
                                    print(val)
                                    add_list_keys = ["PlayersIn","PlayersInvited","PlayersPaid"]
                                    for new_key in add_list_keys:
                                        val[new_key] = []
                                    val["Status"] = "Current"
                                    add_dict_keys = ["Dark","Light"]
                                    for new_key in add_dict_keys:
                                        val[new_key] = {}
                                        val[new_key]["Goalie"] = []
                                        val[new_key]["Line1"] = {"Forward":[],"Defense":[]}
                                        val[new_key]["Line2"] = {"Forward":[],"Defense":[]}
                                    val["Date"] = future_date
                                    val.pop("Enabled",None)
                                    print(val)
                                    print(type(val))
                                    list_of_regulars_emails = []
                                    val, list_of_regulars_emails = check_player_info_for_regular(future_day, val)
                                    print(val, list_of_regulars_emails)
                                    list_of_regulars_emails2 = ["adamwilliams86@yahoo.com"]
                                    print("JUST PRINTED VAL AND REGULARS EMAIL LIST")
                                    all_current_events[new_event_id] = val
                                    print(" WE ARE ABOUT TO SAVE THE AUTOMATED NEW QUICK EVENT INTO THE MYEVENTS FILE")
                                    print(" WE NEED TO ADD THE REGULARS FOR THAT EVENT AND SEND THEM THE EMAIL")
                                    send_new_automated_event_regular_email("Reg", list_of_regulars_emails2, val)
                                    with open('C:\ArizoneChadAPP\myevents.json', 'w') as json_file:
                                        json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                                    break

