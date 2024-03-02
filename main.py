import os



while True:
    print("""
1- Add Employee
2- Add Task 
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