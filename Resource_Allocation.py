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
def backtracking(tasks, employees, constraints):
    def is_complete(assignment):
        return len(assignment) == len(tasks)

    def select_unassigned_task(assignment):
        unassigned_tasks = [task[0] for task in tasks if task[0] not in assignment]
        unassigned_tasks.sort(key=lambda x: x[1])  # Sort tasks by priority
        if unassigned_tasks:
            return unassigned_tasks[0]
        return None

    def is_consistent(task, employee, assignment):
        # Check if the employee is not already assigned to two tasks
        if list(assignment.values()).count(employee) >= 2:
            return False
        # Check if the employee is not assigned the same task as any employee in the constraints
        for constrained_employee, constrained_employees in constraints.items():
            if employee == constrained_employee and task in [t[0] for t in employees[constrained_employee]]:
                return False
            if employee in constrained_employees and task in assignment:
                return False
        return True

    def backtrack(assignment):
        if is_complete(assignment):
            return assignment
        task = select_unassigned_task(assignment)
        if task is None:
            return None  # No unassigned tasks left
        for employee, domain in employees.items():
            if task in [t[0] for t in domain] and is_consistent(task, employee, assignment):
                assignment[task] = employee
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[task]
        return None

    return backtrack({})
solution = backtracking(Tasks, Employee, constrains)
if solution:
    print("Solution:")
    for task, employee in solution.items():
        print(f"{task}: {employee}")
else:
    print("No solution found.")