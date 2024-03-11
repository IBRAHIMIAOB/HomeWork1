import json
#json library for load and dump 
with open("data.json" , "r") as f:
    File:dict = json.loads(f.read())
#Reading data from data.json
TaskName = str(input("Enter Task Name : "))
TaskLocation = str(input("Enter Task Location : "))
TaskRequirement = input("Enter Requirements (Split with ',') : ").split(",")
TaskRequirement = [i.replace(" " , "") for i in TaskRequirement]
#Pull data from user

try:
    TaskPriority = int(input("Enter Task Priority : "))
except Exception:
    print("Not Valid Number")
    exit()
#Check if user entered non-integer 
    
File["Tasks"][TaskName] = {
    "location" : TaskLocation,
    "requirement": TaskRequirement, 
    "priority" : TaskPriority
}
# insert Employee To File
        
with open("data.json" , "w") as f:
    f.write(json.dumps(File , indent=4))
#writing into data.json
