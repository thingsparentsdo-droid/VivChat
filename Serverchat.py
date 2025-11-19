# import statments
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

# ignore this code
def fruitget(fruit):
    with open("Fruit.json") as f:
        data = json.load(f)
        para = [data["Fruits"][fruit]["color"],data["Fruits"][fruit]["shape"],data["Fruits"][fruit]["plant"]]
        return "Color: " + para[0] + ", Shape: " + para[1] + ", Plant: " + para[2]
class FruitData(BaseModel):
    fruit: str


chatserver = FastAPI()

@chatserver.post("/fruitdata")

def fruitdata(data: FruitData):
    fruit = data.fruit
    returndata = fruitget(fruit)
    return returndata

# testing function
@chatserver.get("/test")

def test():
    return {"test":True}

@chatserver.get("/shakesperantrashtalk")

def shakesperantrashtalk():
    
    trash = ["pepper stained dung beetle","eddiwigeing explosive paprica blast storm","denominating expert baha bird","bestowing pizza ballon","experimental parataptat piptin cat","expert testamonial trash talker","gobgob pepel breasted comnom brained bibleflunk","nobodys buisness buisnessman coverd in beeswax","plunging ferret footed pilgrim","forcibly fed faratat disasrer disaster"]
    return("thou art a " + random.choice(trash))



@chatserver.get("/404")

def error404():
    return "error 404 Page Not Found"

@chatserver.get("/scrape")

def scrape(url):
    return requests.get(url)

# function to recive data from inbox

@chatserver.get("/DndGroupChatInbox")
def Messages():
    with open("Chat.json") as f:
        data = json.load(f)
        payload = {
            "Dnd_Group_Chat": data["Dnd_Group_Chat"]
        }
        return payload
    
class MessageData(BaseModel):
    sender: str
    Message: str

# function to send a message

@chatserver.post("/DndGroupChatSendMessage")
def DndGroupChatSendMessage(data: MessageData):
    with open("Chat.json") as f:
        datajson = json.load(f)
        newmessage = {"sender":data.sender,"Message":data.Message}
        datajson["Dnd_Group_Chat"].append(newmessage)
    with open("Chat.json","w") as f:
        json.dump(datajson,f,indent=4)


    






