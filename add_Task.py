import json
with open("data.json" , "r") as f:
    File:dict = json.loads(f.read())
    
TaskName = str(input("Enter Task Name : "))
TaskLocation = str(input("Enter Task Location : "))
TaskRequirement = input("Enter Requirements (Split with ',') : ").split(",")
TaskRequirement = [i.replace(" " , "") for i in TaskRequirement]
try:
    TaskPriority = int(input("Enter Task Priority : "))
except Exception:
    print("Not Valid Number")
    exit()
    
File["Tasks"][TaskName] = {
    "location" : TaskLocation,
    "requirement": TaskRequirement, 
    "priority" : TaskPriority
}
    
with open("data.json" , "w") as f:
    f.write(json.dumps(File , indent=4))
