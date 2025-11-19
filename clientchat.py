# import statments
import requests
import random
import os
import json
# define url and inbox data
URL = 'http://127.0.0.1:8000'
os.system("cls")
def get(CHAT):
    if CHAT == "Dnd_Group_Chat":
        response = requests.get(f"{URL}/DndGroupChatInbox")
        response = response.json()["Dnd_Group_Chat"]
        returntxt = ''
        returntxt += "--- Dnd Group Chat ---\n"
        for i in response:
            returntxt += "("
            returntxt += i['Message']
            returntxt += ")\n"
            returntxt += "|/\n  "
            returntxt += i["sender"] + "\n\n\n"

        return returntxt
    else:
        return "Chat not found"
# main loop

name = input("Enter your name: ")
while True:
    os.system("cls")
    CHAT = "Dnd_Group_Chat"
    print(get(CHAT))

    txt = input()
    if txt == "exit":
        break  
    elif txt == '':
        pass
    else:
        message = {"sender":name,"Message":txt}

        response = requests.post(f"{URL}/DndGroupChatSendMessage",json=message)
