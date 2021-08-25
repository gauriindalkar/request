import requests
import json
import os

if os.path.isfile("courses.json"):
    with open("courses.json","r")as saral_data:
      text_data=json.load(saral_data)

else:
    saral_api= "http://saral.navgurukul.org/api/courses"
    saral_url=requests.get(saral_api)
    data=saral_url.json()
    with open ("courses.json","w")as saral_data:
       text_data=json.dump(data,saral_data,indent=4)

print("")
print("* welcome to navgurukul and learning basic programming language *")
print("")

serial_no=0
for i in text_data["availableCourses"]:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
user_input=int(input("enter your courses number that you want to learn:-"))
parent_id=text_data["availableCourses"][user_input-1]["id"]
parent_name = text_data["availableCourses"][user_input-1]["name"]
print(parent_name)

if os.path.isfile("parents.json"):
    with open("parents.json","r")as saral_data:
      text_data=json.load(saral_data)
else:
    parent_url = "http://saral.navgurukul.org/api/courses/"+str(text_data["availableCourses"][user_input-1]["id"])+"/exercises"
    parent_api = requests.get(parent_url)
    data_1 = parent_api.json()
    with open ("parents.json","w") as saral_data:
        text_data=json.dump(data_1,saral_data,indent=4)
serial_no_1=0
for i in text_data["data"]:
    print("      ",serial_no_1+1,".",i["name"])
    serial_no_1=serial_no_1+1
    if len(i["childExercises"])>0:
        s= 0
        for j in i['childExercises']:
            s = s+ 1
            print( "               ",s,j['name'])
    else:
        print("                1",i["slug"])
        serial_no_1+=1
print("")

if os.path.isfile("contents.json"):
    with open("contents.json","r")as saral_data:
      text_data=json.load(saral_data)

else:
    topic_no = int(input("Enter topic number that's you want to learn:- "))
    m=0 
    list_1=0
    while m<len(text_data["data"][topic_no-1]["childExercises"]):
        print("      ",m+1,data_1["data"][topic_no-1]["childExercises"][m]["name"])
        slug=(text_data["data"][topic_no-1]["childExercises"][m]["slug"])
        content_api=("http://saral.navgurukul.org/api/courses/"+str(parent_id)+'/exercise/getBySlug?slug='+slug)
        content_url=requests.get(content_api)
        data_2=content_url.json()
        with open("contents.json","w") as f2:
            json.dump(text_data,f2,indent=4)
            list_1.append(text_data["content"])
        m=m+1
question_1 = int(input("Enter the question  number: "))
question=question_1-1
print(list_1[question])
while question_1 > 0:
    next_question = input("Do you want next or previous: ").lower()
    if next_question == "p":
        if  question_1 == 1:
            print("no more question")
            break
        elif question_1 > 0:
            question_1 = question_1 - 2
            print(list_1[question_1])
    elif next_question == "n":
        if  question_1 < len(list_1):
            index = question_1 + 1
            print(list_1[index-1])
            question += 1
            question_1 = question_1 + 1
            if question == (len(list_1)-1):
                print("no more question here::")
                break