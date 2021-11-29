
import json
from os import close
import io

f=open('./Src/cfg.json',)

cfg = json.load(f)

#access json parameters using cfg["key"] where cfg is the json object created with json.load()
def setup():
    if cfg["username"]=="":
        name = input("Please enter your name:\n")
        cfg["username"]=name
    if cfg["city"]=="":
        city = input("Please enter the city you live in:\n")
        cfg["city"]=city
    if cfg["pwd"]=="":
        pwd = input("Please enter your password:\n")
        cfg["pwd"]=pwd
    if cfg["email"]=="":
        email = input("Please enter your e-mail adress:\n")
        cfg["email"]=email
    if cfg["phone"]=="":
        phone = input("Please enter your phone number:\n")
        cfg["phone"]=phone
    
    json_string= json.dumps(cfg)
    with open('./Src/cfg.json',"w") as f:
            f.write(json_string)
        

f.close()