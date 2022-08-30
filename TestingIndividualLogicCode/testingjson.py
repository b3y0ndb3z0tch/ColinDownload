import json

#file testingcontacts.json

f = open('../NavigationDrawerButtons.json')
data = json.loads(f.read())
print(data)

# file testingcontacts.json
# [

#   {
#     "playerid": 1,
#     "Player First": "ABC",
#     "Player Last": "ABC",
#     "Cell Number": "123456789",
#     "Email": "fake@gmail.com"
#   },
#   {
#     "playerid": 2,
#     "Player First": "qwe",
#     "Player Last": "qqwwee",
#     "Cell Number": "987654321",
#     "Email": "fake@hotmail.com"
#   }
# ]

if __name__=='__main__':
    f = open('../ContactInfo.json')
    data = json.loads(f.read())
    print(data)
    #NEED TO CHANGE TO CONTACTINFO WHEN DONE TESTING
    f = open("../testingcontacts.json", 'w', encoding='utf-8')
    for player in data:
        if player["Player Last"] == "Williams":
            player["Email"] = "NewFileSaveTest@gmail.com"
            print(player)
    print(json.dumps(data, sort_keys=True, indent=4))
    f.write(json.dumps(data, indent=4))
    f.close()
    f.close()

    # if data.values() == 'Adam':
    #     print(data)
    # if data["Player First"] == 'Adam':
    #     print(data)
    # for i in data:
    #     print(i)
    #     new = i
    #     print(new)
    #     for again in i['contact_list']:
    #         print(again)

