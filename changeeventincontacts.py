import json

# def change_contact_to_quick_events():
#     with open("ContactInfo.json") as f:
#         all_contacts = json.load(f)
#         for single_contact in all_contacts:
#             if single_contact.get("Kroc 0900PM") is not None:
#                 single_contact['KROC 09:00 PM'] = single_contact.get("Kroc 0900PM")
#                 single_contact.pop("Kroc 0900PM")
#             if single_contact.get("Poway 0945PM") is not None:
#                 single_contact['POWAY 09:45 PM'] = single_contact.get("Poway 0945PM")
#                 single_contact.pop("Poway 0945PM")
#             if single_contact.get("UTC 1030PM") is not None:
#                 single_contact['UTC 10:30 PM'] = single_contact.get("UTC 1030PM")
#                 single_contact.pop("UTC 1030PM")
#             with open('ContactInfo.json', 'w') as json_file:
#                 json.dump(all_contacts, json_file, indent=4, separators=(',', ':'))
#
# change_contact_to_quick_events()

##TO CHANGE THE MONIES STRING TO INTS OF CURRENT CONTACT INFO
# def change_monies_to_int():
#     with open("ContactInfo.json") as f:
#         all_contacts = json.load(f)
#         for single_contact in all_contacts:
#             print(type(single_contact.get("Monies")))
#             if isinstance(single_contact.get("Monies"), str):
#                 single_contact['Monies'] = 0
#             with open('ContactInfo.json', 'w') as json_file:
#                 json.dump(all_contacts, json_file, indent=4, separators=(',', ':'))
#
# change_monies_to_int()