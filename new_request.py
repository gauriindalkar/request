import requests
import json

saral_url="http://saral.navgurukul.org/api/courses"
saral_api=requests.get(saral_url)
data=saral_api.json()

with open("courses_1.json","w") as f:
    json.dump(data,f,indent=4)  

print("")
print("* Welcome to navgurukul and Learn basic programming launguage ")
print("")

seriol_no=0
for i in data["availableCourses"]:
    print(seriol_no+1,i["name"],i["id"])
    seriol_no=seriol_no+1
cources_name=int(input("select a cources which you want to learn: "))
cource_1=data["availableCourses"][cources_name-1]["name"]
print(cource_1)

parentes_api= "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][cources_name-1]["id"])+"/exercises"
parentes_url=requests.get(parentes_api)
data_1=parentes_url.json()

with open("parentes_1.json","w") as f1:
    json.dump(data_1,f1,indent=4)

j=0
for i in data_1["data"]:
    print("   ",j+1,".",i["name"])
    if len(i["childExercises"])==0:
        slug=(data_1["data"][j-1]["slug"])
        print("        1.",slug)
    else:
        l=0
        while l<len(data_1["data"][j]["childExercises"]):
            child=data_1["data"][j]["childExercises"][l-1]["name"]
            print("            ",l+1,".",child)
            l=l+1
    j=j+1
topic_no = int(input("Enter topic number that's you want to learn:- "))
m=0 
list_1=0
while m<len(data_1["data"][topic_no-1]["childExercises"]):
    print("      ",m+1,data_1["data"][topic_no-1]["childExercises"][m]["name"])
    slug=(data_1["data"][topic_no-1]["childExercises"][m]["slug"])
    content_api=("http://saral.navgurukul.org/api/courses/"+str(parents_id)+'/exercise/getBySlug?slug='+slug)
    content_url=requests.get(content_api)
    data_2=content_url.json()
    with open("content_1.json","w") as f2:
        json.dump(data_2,f2,indent=4)
        list_1.append(data_2["content"])
    m=m+1

content1=int(input('enter the question number:'))
question=content1-1
print(list_1[question])
while content1>0:
    next=input("enter the next p/n")
    if content1==len(list_1):
        print("next npage")
    if next=="p":
        if content1==1:
            print("no more question")
            break
        elif content1>0:
            content1=content1-1
            print(list_1[content1])
    elif next=="n":
        if content1<len(list_1):
            index=content1+1
            print(list_1[index-1])
            question=question+1
            content1+=1
            break
    elif question==(len(list_1))-1:
                print("next page")
                break
    



