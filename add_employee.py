import json 
#json library for load and dump 
with open("data.json" , "r") as f :
    File :dict = json.loads(f.read())
#Reading data from data.json
EmployeeName = str(input("Enter Employee Name : "))
EmployeeMajor = str(input("Enter Employee Major : ")).upper()
EmployeeLocation = str(input("Enter Employee Location :"))
EmployeeDomain = File.get("Tasks").keys()
#Pull data from user
tempTask = []
for i in EmployeeDomain : 
    if EmployeeLocation == File.get("Tasks").get(i).get("location") and EmployeeMajor  in File.get("Tasks").get(i).get("requirement") :
        tempTask.append(i)
#calculating Employee domain
File["Employee"][EmployeeName] = {
        "major": EmployeeMajor ,
        "location":EmployeeLocation,
        "domain": tempTask
    }
# insert Employee To File


with open("data.json" , "w") as f :
    f.write(json.dumps(File , indent=4))
#Writing To File

print("Employee Added")

