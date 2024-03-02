import json 


with open("data.json" , "r") as f :
    File :dict = json.loads(f.read())

EmployeeName = str(input("Enter Employee Name : "))
EmployeeMajor = str(input("Enter Employee Major : ")).upper()
EmployeeLocation = str(input("Enter Employee Location :"))
EmployeeDomain = File.get("Tasks").keys()
tempTask = []
for i in EmployeeDomain : 
    if EmployeeLocation == File.get("Tasks").get(i).get("location") and EmployeeMajor  in File.get("Tasks").get(i).get("requirement") :
        tempTask.append(i)

File["Employee"][EmployeeName] = {
        "major": EmployeeMajor ,
        "location":EmployeeLocation,
        "domain": tempTask
    }
# for employee in File["Employee"].keys():
#     tempList = []
#     for otherEmployee in File["Employee"].keys():
#         if File["Employee"][employee].get("location") == File["Employee"][employee].get("location"):
#             tempList.append(otherEmployee)
#     File["Employee"][employee]["constrains"] = tempList

with open("data.json" , "w") as f :
    f.write(json.dumps(File , indent=4))

print("Employee Added")

