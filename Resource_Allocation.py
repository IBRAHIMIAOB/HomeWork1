import json , copy
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
    
    else:
        return

def backTrack(employees, tasks, constraints, assignment=None, solutions=None, solution_limit=None):
    if assignment is None:
        assignment = {}
    if solutions is None:
        solutions = []
    if solution_limit is None:
        solution_limit = float('inf')  # No limit by default

    Flag = True
    for emp in employees.keys():
        if employees.get(emp) != []:
            Flag = False
            break
    if Flag:
        solutions.append(assignment)
        print(assignment)
        if len(solutions) >= solution_limit:
            return solutions

    tasksCount = {employee: len(assignment.get(employee, [])) for employee in employees}
    sortedEmployees = sorted(employees.keys(), key=lambda x: tasksCount.get(x, 0))

    for employee in sortedEmployees:
        for task in employees.get(employee):
            newEmployees = copy.deepcopy(employees)
            newTasks = tasks.copy()
            newAssignment = copy.deepcopy(assignment)

            reduce(employee, task, newEmployees, newTasks, constraints, newAssignment)

            solutions = backTrack(newEmployees, newTasks, constraints, newAssignment, solutions, solution_limit)
            if len(solutions) >= solution_limit:
                return solutions

    return solutions
limit = int(input("ENTER LIMIT: "))
solutions = backTrack(Employee , Tasks , constrains , solution_limit=limit)
for i, solution in enumerate(solutions, start=1):
    print("solution #", i , " :")
    for j in solution:
        print(j  , solution.get(j))
    print()

