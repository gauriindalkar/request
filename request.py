import requests
import json

saral_url="http://saral.navgurukul.org/api/courses"
saral_api=requests.get(saral_url)
Data=saral_api.json()

with open("courses_data.json","w") as f:
    json.dump(Data,f,indent=4)  

print("")
print("* Welcome to navgurukul and Learn basic programming launguage ")
print("")

serial_no = 0
for i in Data['availableCourses']:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
print(" ")
cources_name=int(input("select a cources which you want to learn: "))
cource_1=Data["availableCourses"][cources_name-1]["name"]
parents_id=Data["availableCourses"][cources_name-1]["id"]
print(cource_1)

user_input_1=input("Do you wants to continue with this course or not?just say yes or no: "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ).lower()
if user_input_1=="no":
    for i in Data["availableCourses"]:
        print(serial_no+1,i["name"],i["id"])
        serial_no=serial_no+1
    user_input=int(input("select a cources which you want to learn: "))
    print(Data["availableCourses"][user_input-1]["name"])

parentes_api= "http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][cources_name-1]["id"])+"/exercises"
parentes_url=requests.get(parentes_api)
data_1=parentes_url.json()
with open("parentes_data.json","w") as file:
    json.dump(data_1,file,indent=4)

j=0
for i1 in data_1["data"]:
    print("   ",j+1,".",i1["name"])
    if len(i1["childExercises"])==0:
        slug=(data_1["data"][j-1]["slug"])
        print("        1.",slug)
    else:
        l=0
        while l<len(data_1["data"][j]["childExercises"]):
            child=data_1["data"][j]["childExercises"][l-1]["name"]
            print("            ",l+1,".",child)
            l=l+1
    j=j+1
print(" ")
topic_no=int(input("Enter exercise number which you want to solve: "))
serial_no_3=0
my_list=[]
for l in data_1["data"]:
    serial_no_3=+1
    if topic_no==serial_no_3:
        user_input_3=input("Enter topic number that's you want to learn previous or next:- ")
        if user_input_3=="p":
            j=0
            for i in data_1["data"]:
                print("   ",j+1,".",i["name"])
                if data_1["data"][j]["childExercises"]==[]:
                    slug=(data_1["data"][j]["slug"])
                    print("        1.",slug)
                else:
                    l=0
                    while l<len(data_1["data"][j]["childExercises"]):
                        child=data_1["data"][j]["childExercises"][l]["name"]
                        print("            ",l+1,".",child)
                        l=l+1
                    j=j+1
                topic_no = int(input("Enter topic number that's you want to learn:- "))
m=0 
while m<len(data_1["data"][topic_no-1]["childExercises"]):
    print("      ",m+1,data_1["data"][topic_no-1]["childExercises"][m]["name"])
    slug=(data_1["data"][topic_no-1]["childExercises"][m]["slug"])
    child_exercise=("http://saral.navgurukul.org/api/courses/"+str(parents_id)+'/exercise/getBySlug?slug='+slug)
    child_exercise_url=requests.get(child_exercise)
    data_2=child_exercise_url.json()
    with open("topic.json","w") as fi:
        json.dump(data_2,fi,indent=4)
        my_list.append(data_2["content"])
    m=m+1

content1=int(input('enter the question number: '))
question=content1-1
print(my_list[question])
while content1>0:
    next=input("enter the next p/n")
    if content1==len(my_list):
        print("next npage")
    if next=="p":
        if content1==1:
            print("no more question")
            break
        elif content1>0:
            content1=content1-2
            print(my_list[content1])
    elif next=="n":
        if content1<len(my_list):
            index=content1+1
            print(my_list[index-1])
            question=question+1
            content1+=1
            if question==(len(my_list))-1:
                print("next page")
                break
    


