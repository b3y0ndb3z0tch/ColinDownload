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
from alerts import email_alert

# list_of_regulars_emails2 used for testing
# NEEDS TO BE REPLACED WITH list_of_regulars_emails WHICH IS NEW INVITED PLAYERS EMAILS

def check_if_event_already_made(future_date):
    with open('C:\kivymd\ChadAPP\myevents.json') as allcurrentevents:
        all_current_events = json.load(allcurrentevents)
        print("****   IN THE check_if_event_already_made MODULE   ***")
        print(type(future_date))
        print(future_date)
        for key, val in all_current_events.items():
            print(key,val)
            if isinstance(val, dict):
                print("yes the value of the key is a dictionary")
                for key2, val2 in val.items():
                    if key2 == "Date":
                        print("222 KEY IS DATE 222")
                        print(val2)
                        print(type(val2))
                        print("just printed val2 and type")
                        if val2 == future_date:
                            print("EVENT ALREADY CREATED")
                            return False
    print("1"*100)
    return True

def check_player_info_for_regular(future_day, val):
    print("***   IN THE check_player_info_for_regular MODULE RETURNS val AND list_of_regulars_emails   ***")
    with open('C:\kivymd\ChadAPP\ContactInfo.json') as listofplayers:
        list_of_all_players = json.load(listofplayers)
        list_of_regulars_emails = []
        for player in list_of_all_players:
            if player.get(future_day) == "R":
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
    with open("C:\kivymd\ChadAPP\standardmessages.json") as file:
        all_messages = json.load(file)
        email_message = all_messages[val["Day"] + "Reg"].replace("insert_date", future_date)
        for player in list_of_regulars_emails:
            email_alert(player, "Test Email", email_message)

def check_current_day_for_new_event():
    for a in range(1,7):
        future_date, future_day = create_future_date_and_future_day(a)
        with open("C:\kivymd\ChadAPP\quickevents.json") as f:
            quick_events = json.load(f)
            print(quick_events)
            for key, val in quick_events.items():
                print(key,val)
                if isinstance(val, dict):
                    for key2, val2 in val.items():
                        print(key2,val2)
                        print(type(val2))
                        if key2 == "Day" and val2 == future_day:
                            print("%%% JUST CHECKED QUICK EVENT DAY TO FUTURE DAY &&&")
                            print(key)
                            print(val)
                            print(val2)
                            print(val["Enabled"])
                            if check_if_event_already_made(future_date):
                                with open('C:\kivymd\ChadAPP\myevents.json') as allcurrentevents:
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
                                    list_of_regulars_emails = []
                                    val, list_of_regulars_emails = check_player_info_for_regular(future_day, val)
                                    print(val, list_of_regulars_emails)
                                    list_of_regulars_emails2 = ["adamwilliams86@yahoo.com"]
                                    print("JUST PRINTED VAL AND REGULARS EMAIL LIST")
                                    all_current_events[new_event_id] = val
                                    print(" WE ARE ABOUT TO SAVE THE AUTOMATED NEW QUICK EVENT INTO THE MYEVENTS FILE")
                                    print(" WE NEED TO ADD THE REGULARS FOR THAT EVENT AND SEND THEM THE EMAIL")
                                    print(val["Day"]+"Reg")
                                    send_new_automated_event_regular_email(val, list_of_regulars_emails2, future_date)
                                    with open('C:\kivymd\ChadAPP\myevents.json', 'w') as json_file:
                                        json.dump(all_current_events, json_file, indent=4, separators=(',', ':'))
                                    break

check_current_day_for_new_event()
