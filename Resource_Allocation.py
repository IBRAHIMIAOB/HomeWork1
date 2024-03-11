import json 
#json library for load and dump 
with open("data.json" , 'r') as f:          
    File :dir = json.loads(f.read())
#Reading data from data.json
Tasks :list= [(task , File["Tasks"][task]["priority"]) for task  in File["Tasks"].keys()] 
#setting Task List from File : list(str)


Employee : dict[str , any] = {}
for Employee1 in File["Employee"].keys():
    Employee[Employee1] = [(task , File["Tasks"][task]["priority"]) for task in File["Employee"][Employee1]["domain"] ]
#setting Employee List :  dict[str , list(str)]
constrains : dict[str , list[str]] = {}
for Employee1 in File["Employee"].keys():
    tempList = []
    for other in File["Employee"].keys():
        if File["Employee"][Employee1]["location"] == File["Employee"][other]["location"] :
            tempList.append(other)
    tempList.remove(Employee1)
    constrains[Employee1] = tempList
#setting constrains  dict[str , list[str]]

# Functions of BackTracing


def reduce(employee , task , employeeList , taskList , constrains ,assignment):
    if task not in employeeList[employee]:
        print(f"{task} is not in {employeeList[employee]}")
        return
    
    #constrains reduction
    for otherEmployee in constrains[employee]:
        removedTask = []
        TaskList =assignment.get(otherEmployee)
        if TaskList:
            for Task in employeeList.get(employee):
                if Task in TaskList:
                    removedTask.append(Task)
            for Task in removedTask:
                employeeList[employee].remove(Task)
                
                
    
    
    
    if task in employeeList.get(employee):
        if assignment.get(employee):
            assignment.get(employee).append(task)
        else:
            assignment[employee] = [task]
        employeeList.get(employee).remove(task)
        taskList.remove(task)
    else :
        return

def backTrack(Employee , Tasks , constrains  , assignment = {} , solutions = []):
    if len(Tasks) == 0:
       solutions.append(assignment)
       return
    
    for employee in Employee.keys():
        for task in Employee.get(employee):
            newEmployee = Employee.copy()
            newTasks = Tasks.copy()
            newassignment = assignment.copy()
            reduce(employee , task , newEmployee , newTasks , constrains , newassignment)
            backTrack(newEmployee  , newTasks , constrains , newassignment)
    
    return solutions
x = backTrack(Employee , Tasks , constrains)

for i in x: 
    print(i)
    

