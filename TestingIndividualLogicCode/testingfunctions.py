from datetime import datetime, timedelta
import json
from functools import partial
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton




def remove_nav_drawer_3_widgets(self):
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite)
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite2)
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite3)
    self.root.ids.nav_drawer3_md_list.remove_widget(self.invite4)


def closeLeftDrawerQuickButtons(self):
        self.root.ids.left_md_list.remove_widget(self.addquickeventbutton)
        self.root.ids.left_md_list.remove_widget(self.addquickeventbutton2)
        self.root.ids.left_md_list.remove_widget(self.addquickeventbutton3)
        self.root.ids.nav_drawer.set_state('close')


def find_current_date_quick_event_date(self, quick_day):
    print("!!!   find_current_date_quick_event_date Module   !!!")
    dt = datetime.now()

    for a in range(1,8):
        future_date = dt + timedelta(days=a)
        future_day = future_date.strftime('%A').upper()
        future_date = future_date.strftime("%x")
        print(future_date, future_day)
        if quick_day == future_day:
            self.root.ids.date.text = future_date
            return


def regular_email_date_insert_day(self,day):
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

def format_time(self, time):
    print("!!!   format_time Module   !!!")
    print(time)
    print(len(time))
    if len(time) == 8 and time[2] == ":" and time[5] == " ":
        print("The time is properly formatted")
        return time
    if len(time) != 8:
        print("the string needs to be formatted")
        if time[2] != ":":
            time = time[:2] + ":" + time[2:]
            print(time)
        if time[5] != " ":
            time = time[:5] + " " + time[5:]
            print(time)
    print(len(time))
    format_time(self, time)
    return time.upper()


def format_date(self, date):
    print("!!!   format_date Module   !!!")
    print(date)
    print(len(date))
    if len(date) == 8 and date[2] == "/" and date[5] == "/":
        print("date is formmated correctly")
        return date
    if len(date) != 8:
        print("the date needs to be formatted")
        if date[2] != "/":
            date = date[:2] + "/" + date[2:]
            print(date)
        if date[5] != "/":
            date = date[:5] + "/" + date[5:]
            print(date)
    print(len(date))
    format_date(self, date)


def add_new_buttons(self,root):
    print("*!*"*250)
    with open("new_buttons.json") as file:
        new_buttons = json.load(file)
        count = "0"
        for button, action in new_buttons.items():
            self.new_button = MDRaisedButton(font_style='Subtitle2', text=button,
                                               on_press=partial(action),
                                               size_hint=(1, None), padding='10dp', anchor_x='left',
                                               md_bg_color=(.87, .36, .24, 1))

def remove_edit_submit(self,root):
    for child in self.root.ids.edit_quick_event_layout2.children[:]:
        print(child)
        if isinstance(child, MDFillRoundFlatButton):
            self.root.ids.edit_quick_event_layout2.remove_widget(child)

def clear_quick_event_text_fields(self,root):
    self.root.ids.quick_time.text = ""
    self.root.ids.quick_day.text = ""
    self.root.ids.quick_location.text = ""
    self.root.ids.quick_cost.text = ""
    self.root.ids.quick_totalplayers.text = ""


def add_quick_event_to_player_dict(self, contact_dict, quick_event_dict, quick_event_name):
    print("%%%   add_quick_event_to_player_dict MODULE   %%%")
    for single_contact in contact_dict:
        for single_event in quick_event_dict.keys():
            if single_contact.get(single_event) is not None:
                print("%%%")
                if single_contact[single_event] == "R":
                    single_contact[quick_event_name] = "R"
                    print("%")
                if single_contact[single_event] == "S":
                    single_contact[quick_event_name] = "S"
                    print("%%%%%%%%%%%%%%%%%%")
            else:
                single_contact[quick_event_name] = ""
                print("***")
    print("*"*350)
    print(contact_dict)
    return contact_dict

def replace_email_message(self, dict_of_event, txt):
    txt = txt.replace("insert_date", str(dict_of_event.get("Date")))
    print(txt)
    email_by_date = str(regular_email_date_insert_day(self, dict_of_event.get("Day")))
    txt = txt.replace("insert_email_by_date", email_by_date)
    txt = txt.replace("insert_day", self.dict_of_event.get("Day"))
    txt = txt.replace("insert_location", self.dict_of_event.get("Location"))
    txt = txt.replace("insert_time", self.dict_of_event.get("Time"))
    return txt


def check_if_list_or_dict(self, key, val, player_id):
    if isinstance(val, list):
        print(val)
        print(type(val))
        print("*"*250)
        if len(val) != 0:
            for number in val:
                if player_id == number:
                    print("PLAYER ALREADY INVITED")
                    return True
                else:
                    print(" WE MADE IT INTO HERE AND PLAYER STILL NOT INVITED ")
        else:
            print("THE LIST WAS EMPTY")
    if isinstance(val, dict):
        for key2, val2 in val.items():
            print("****RECURSIVE*****")
            check_if_list_or_dict(self, key2, val2, player_id)





def check_if_player_invited(self, this_event, player_id):
    print("!!!   check_if_player_invited MODULE   !!!")
    print(player_id)
    for key, val in this_event.items():
        print(key, val)
        if(check_if_list_or_dict(self, key, val, player_id)):
            return True
            print("WE MADE IT ALL THE WAY TO THE END OF CHECKING")
            print("NEED TO RETURN FALSE SO THAT THE PLAYER WILL BE INVITED")

def check_if_list(self, key, val, this_event, players_to_pay):
    print("in the check_if_list function")
    if isinstance(val, list):
        print(val)
        print(type(val))
        print("*"*250)
        if len(val) != 0:
            for number in val:
                if number in this_event['PlayersPaid']:
                    print("ABOUT TO BREAK")
                    break
                else:
                    players_to_pay.append(number)
                    #ADD PLAYER TO SWIPECARD TO THE SCREEN
        else:
            print("THE LIST WAS EMPTY")
    if isinstance(val, dict):
        for key2, val2 in val.items():
            print("****RECURSIVE*****")
            check_if_list(self, key2, val2, this_event, players_to_pay)
    return players_to_pay

def add_player_to_payment_screen(self, this_event):
    print("+++   in the add_player_to_payment_screen MODULE   +++")
    players_to_pay = []
    for key, val in this_event.items():
        if isinstance(val, dict):
            players_to_pay = check_if_list(self, key, val, this_event, players_to_pay)
    return players_to_pay


