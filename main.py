import os



while True:
    print("""
1- Add Employee
2- Add Task 
3- Resource Allocation
          """)
    try:
        Choice = int(input("Enter Input : ")) 
    except Exception: 
        print("wrong Input")
        continue 
    
    if Choice  == 1: 
        os.system("python add_employee.py")
    elif Choice == 2 :
        os.system("python add_Task.py")
    elif Choice == 3: 
        os.system("python Resource_Allocation.py")