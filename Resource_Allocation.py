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


def reduce(employee, task, employeeList, taskList, constraints, assignment):
    if task not in employeeList[employee]:
        print(f"{task} is not in {employeeList[employee]}")
        return
    
    # Constraints reduction
    for otherEmployee in constraints[employee]:
        removedTasks = []
        taskListOther = assignment.get(otherEmployee)
        if taskListOther:
            for taskOther in employeeList.get(employee):
                if taskOther in taskListOther:
                    removedTasks.append(taskOther)
            for taskOther in removedTasks:
                employeeList[employee].remove(taskOther)
                
    if task in employeeList.get(employee):
        if assignment.get(employee):
            assignment[employee].append(task)
        else:
            assignment[employee] = [task]
        employeeList[employee].remove(task)
        taskList.remove(task)
    else:
        return

def backTrack(employees, tasks, constraints, assignment=None, solutions=None):
    if assignment is None:
        assignment = {}
    if solutions is None:
        solutions = []

    if len(tasks) == 0:
        solutions.append(assignment)
        return
    
    # Count tasks assigned to each employee
    tasksCount = {employee: len(assignment.get(employee, [])) for employee in employees}

    # Sort employees based on the number of assigned tasks (ascending order)
    sortedEmployees = sorted(employees.keys(), key=lambda x: tasksCount.get(x, 0))

    for employee in sortedEmployees:
        for task in employees.get(employee):
            newEmployees = employees.copy()
            newTasks = tasks.copy()
            newAssignment = assignment.copy()
            reduce(employee, task, newEmployees, newTasks, constraints, newAssignment)
            backTrack(newEmployees, newTasks, constraints, newAssignment, solutions)
    
    return solutions

solutions = backTrack(Employee , Tasks , constrains)
for i, solution in enumerate(solutions, start=1):
    print(f"Solution {i}: {solution}")

