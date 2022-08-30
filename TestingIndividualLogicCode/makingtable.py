def email_message_body(messages, dict_of_event, current_event_day):
    print(" in the email_message_body")
    specific_message = f'{current_event_day}Fin'
    txt = str(messages[2].get(specific_message))
    txt = txt.replace("insert_date", str(dict_of_event.get("Date")))
    txt = txt.replace("insert_day", str(dict_of_event.get("Day")))
    txt = txt.replace("insert_time", str(dict_of_event.get("Time")))
    txt = txt.replace("insert_location", str(dict_of_event.get("Location")))
    print(txt)
    print("just printed txt")
    return txt

def email_players_and_table(all_contact_info, dict_of_event):
    print(" in the email_players_and_table")
    players_assigned_to_teams = []
    table_to_insert = ""
    table_to_insert += '<style type="text/css"> .tg  {border-collapse:collapse;border-spacing:0; width:50%; background-color:#3489bb;} .tg td{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:14px; ;  overflow:hidden;padding:10px 5px;word-break:normal;}.tg th{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:14px;  font-weight:heavy;overflow:hidden;padding:10px 5px;word-break:normal;}  .tg th2{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:20px;  font-weight:heavy;overflow:hidden;padding:10px 5px;word-break:normal;}.tg .tg-0pky{border-color:inherit;text-align:center;vertical-align:top}'
    table_to_insert += ' .tg2  {border-collapse:collapse;border-spacing:0; width:50%; background-color:#df5d3b;} .tg2 td{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:14px; ;  overflow:hidden;padding:10px 5px;word-break:normal;}.tg2 th{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:14px;  font-weight:heavy;overflow:hidden;padding:10px 5px;word-break:normal;}  .tg2 th2{border-color:black;border-style:solid;border-width:3px;font-family:Arial, sans-serif;font-size:20px;  font-weight:heavy;overflow:hidden;padding:10px 5px;word-break:normal;}.tg2 .tg2-0pky{border-color:inherit;text-align:center;vertical-align:top}</style>'
    table_to_insert += '<table class="tg"><thead><tr style="background-color:#3489bb;"><th align="center" class="tg-0pky" colspan="4">Dark Team</th></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky">Goalie:</th><td class="tg-0pky" colspan="3">dark_goalie</td></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky" colspan="4">		Line 1	</th></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky">		Forwards:	</th>	<td class="tg-0pky">		insert_dark_forward	</td>	<td class="tg-0pky">		insert_dark_forward	</td>	<td class="tg-0pky">		insert_dark_forward	</td></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky" colspan="2">		Defense:	</th>	<td class="tg-0pky" colspan="1">		insert_dark_defense	</td>	<td class="tg-0pky" colspan="1">		insert_dark_defense	</td></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky" colspan="4">		Line 2	</th></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky">		Forwards:	</th>	<td class="tg-0pky">		insert_dark_forward2	</td>	<td class="tg-0pky">		insert_dark_forward2	</td>	<td class="tg-0pky">		insert_dark_forward2	</td></tr><tr style="background-color:#3489bb;">	<th class="tg-0pky" colspan="2">		Defense:	</th>	<td class="tg-0pky" colspan="1">		insert_dark_defense2	</td>	<td class="tg-0pky" colspan="1">		insert_dark_defense2	</td></tr></thead></table>'
    table_to_insert += '<table class="tg2"><thead><tr>	<th align="center" class="tg2-0pky" colspan="4">		Light Team	</th></tr><tr>	<th class="tg2-0pky">		Goalie:	</th>	<td class="tg2-0pky" colspan="3">		light_goalie	</td></tr><tr>	<th class="tg2-0pky" colspan="4">		Line 1	</th></tr><tr>	<th class="tg2-0pky">		Forwards:	</th>	<td class="tg2-0pky">		insert_light_forward	</td>	<td class="tg2-0pky">		insert_light_forward	</td>	<td class="tg2-0pky">		insert_light_forward	</td></tr><tr>	<th class="tg2-0pky" colspan="2">		Defense:	</th>	<td class="tg2-0pky" colspan="1">		insert_light_defense	</td>	<td class="tg2-0pky" colspan="1">		insert_light_defense	</td></tr><tr>	<th class="tg2-0pky" colspan="4">		Line 2	</th></tr><tr>	<th class="tg2-0pky">		Forwards:	</th>	<td class="tg2-0pky">		insert_light_forward2	</td>	<td class="tg2-0pky">		insert_light_forward2	</td>	<td class="tg2-0pky">		insert_light_forward2	</td></tr><tr>	<th class="tg2-0pky" colspan="2">		Defense:	</th>	<td class="tg2-0pky" colspan="1">		insert_light_defense2	</td>	<td class="tg2-0pky" colspan="1">		insert_light_defense2	</td></tr></thead></table>'
    for a in dict_of_event['Dark'].get('Goalie'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("dark_goalie", name)
    for a in dict_of_event['Dark']['Line1'].get('Forward'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_dark_forward", name, 1)
    for a in dict_of_event['Dark']['Line1'].get('Defense'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_dark_defense", name, 1)
    for a in dict_of_event['Dark']['Line2'].get('Forward'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_dark_forward2", name, 1)
    for a in dict_of_event['Dark']['Line2'].get('Defense'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_dark_defense2", name, 1)
    for a in dict_of_event['Light'].get('Goalie'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("light_goalie", name)
    for a in dict_of_event['Light']['Line1'].get('Forward'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_light_forward", name, 1)
    for a in dict_of_event['Light']['Line1'].get('Defense'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_light_defense", name, 1)
    for a in dict_of_event['Light']['Line2'].get('Forward'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_light_forward2", name, 1)
    for a in dict_of_event['Light']['Line2'].get('Defense'):
        players_assigned_to_teams.append(a)
        name = str(all_contact_info[a - 1].get("Player First"))
        name += " " + str(all_contact_info[a - 1].get("Player Last"))
        table_to_insert = table_to_insert.replace("insert_light_defense2", name, 1)
    return players_assigned_to_teams, table_to_insert

def current_event_title_bar(dict_of_event):
    print(" in the current_event_title_bar")
    labeltext = f" {dict_of_event.get('Date')}"
    labeltext += f" {dict_of_event.get('Day')}"
    labeltext += f" {dict_of_event.get('Location')}"
    labeltext += f" {dict_of_event.get('Time')}"
    labeltext += f"\nInvited: {len(dict_of_event.get('PlayersInvited'))}"
    labeltext += f" ~ Assign: {len(dict_of_event.get('PlayersIn'))}"
    labeltext += f" ~ Goalies: {len(dict_of_event['Dark'].get('Goalie')) + len(dict_of_event['Light'].get('Goalie'))} \n" \
                 f"Dark: {len(dict_of_event['Dark']['Line1'].get('Forward')) + len(dict_of_event['Dark']['Line1'].get('Defense')) + len(dict_of_event['Dark']['Line2'].get('Forward')) + len(dict_of_event['Dark']['Line2'].get('Defense'))}" \
                 f" ~ Light: {len(dict_of_event['Light']['Line1'].get('Forward')) + len(dict_of_event['Light']['Line1'].get('Defense')) + len(dict_of_event['Light']['Line2'].get('Forward')) + len(dict_of_event['Light']['Line2'].get('Defense'))}"
    return labeltext

def organize_attendee_title_bar(dict_of_event):
    print("in the organize_attendee_title_bar")
    labeltext = f" {dict_of_event.get('Date')}"
    labeltext += f" {dict_of_event.get('Day')}"
    labeltext += f" {dict_of_event.get('Location')}"
    labeltext += f" {dict_of_event.get('Time')}"
    labeltext += f"\nDGoalie: {len(dict_of_event['Dark'].get('Goalie'))} "
    labeltext += f"~ LGoalie: {len(dict_of_event['Light'].get('Goalie'))} "
    labeltext += f"\nDL1F: {len(dict_of_event['Dark']['Line1'].get('Forward'))} ~ DL2F: {len(dict_of_event['Dark']['Line2'].get('Forward'))}"
    labeltext += f" ~ DL1D: {len(dict_of_event['Dark']['Line1'].get('Defense'))} ~ DL2D: {len(dict_of_event['Dark']['Line2'].get('Defense'))}"
    labeltext += f"\nLL1F: {len(dict_of_event['Light']['Line1'].get('Forward'))} ~ LL2F: {len(dict_of_event['Light']['Line2'].get('Forward'))}"
    labeltext += f" ~ LL1D: {len(dict_of_event['Light']['Line1'].get('Defense'))} ~ LL2D: {len(dict_of_event['Light']['Line2'].get('Defense'))}"
    return labeltext

def organize_attendee_player_card(all_current_events, all_contact_info, current_event_identify,a):
    print("in the organize_attendee_player_card")
    print(a)
    name = all_contact_info[a - 1].get("Player First")
    name += " " + all_contact_info[a - 1].get("Player Last")
    positionstring = "Pos: "
    positionstring += f'{all_contact_info[a - 1].get("position F D G")}'
    positionstring += "  Line: "
    positionstring += f'{all_contact_info[a - 1].get("LINE")}'
    randomtext = "Random Text for third line"
    return name, positionstring, randomtext

def organize_player_invited_player_card(all_contact_info, dict_of_event, a):
    print("*" * 250)
    print("in the organize_player_invited_player_card in the back_to_current_event function")
    print(all_contact_info[a - 1])
    namestring = "Name: "
    namestring += f"{all_contact_info[a - 1].get('Player First')}"
    namestring += " " + f"{all_contact_info[a - 1].get('Player Last')}"
    positionstring = "Pos: "
    positionstring += f'{all_contact_info[a - 1].get("position F D G")}'
    positionstring += "  Line: "
    positionstring += f'{all_contact_info[a - 1].get("LINE")}'
    player_id = int(all_contact_info[a - 1].get("playerid"))
    return namestring, positionstring, player_id

def testing_key_word_args(*args):
    with open("standardmessages.json") as allstandardmessages:
        for a in allstandardmessages:
            print(a)