import requests
import json
import os

if os.path.isfile("courses.json"):
    with open("courses.json","r")as saral_data:
        data=json.load(saral_data)

else:
    saral_api= "http://saral.navgurukul.org/api/courses"
    saral_url=requests.get(saral_api)
    data=saral_url.json()
    with open ("courses.json","w")as saral_data:
        json.dump(data,saral_data,indent=4)

print("")
print("* welcome to navgurukul and learning basic programming language *")
print("")

serial_no=0
for i in data["availableCourses"]:

    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1

user_input=int(input("enter your courses number that you want to learn:-"))
cource_1=data["availableCourses"][user_input-1]["name"]
print(cource_1)
