#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 09/23/24
#Description: This program reads a file and creates a tasklist. The user can add, mark, remove, and save tasks. 
from task import Task
import check_input

def main_menu():
    """
    Description: display the main menu and the number of task
    Parameters: None
    Return: choice - int
    """
    print ("--TASKLIST--")
    taskfile = open("tasklist.txt", 'r')
    numoftask = 0
    for line in taskfile:
        if line != "\n":
            numoftask +=1
        elif line == "\n":
            numoftask += 0
    print(f"You have {numoftask} tasks.")
    choice = check_input.get_int_range("1. Display current task \n2. Mark current task as complete \n3. Postpone current task \n4. Add new task \n5. Save and Quit \nEnter choice: ", 1,5)
    return choice

def read_file():
    """
    Description: read the file 
                 create a Task object for each line in file
                 save Task objects in tasklist
    Parameters: None
    Return: tasklist - list
    """
    tasklist = []
    with open('tasklist.txt', 'r') as taskfile: 
        for line in taskfile:
            if line != "\n":
                str = line.strip()
                tasklist.append(Task(*str.split(',')))
        taskfile.close()
    tasklist.sort()
    return (tasklist)

def write_file(tasklist):
    """
    Description: write the tasks in tasklist into the file
    Parameters: tasklist - list
    Return: None
    """
    file = open('tasklist.txt', 'w')
    for i in range(len(tasklist)):
        task_ = Task(tasklist[i].desc, tasklist[i].date, tasklist[i].time)
        file.write(f"{repr(task_)}\n")
    file.close()

def get_date():
    """
    Description: prompt the user to enter new day, month, year for task
    Parameters: None
    Return: date - string
    """
    print("Enter due date for your task.")
    month_int = check_input.get_int_range(("Enter month: "), 1, 12)
    day_int = check_input.get_int_range(("Enter date: "), 1, 31)
    year_int = check_input.get_int_range(("Enter year: "), 2000, 2100)

    month = str(month_int)
    day = str(day_int)
    year = str(year_int)

    if month_int < 10 :
        month = "0" + str(month_int)
    if day_int < 10:
        day = "0" + str(day_int)

    return f"{month}/{day}/{year}"

def get_time():
    """
    Description: prompt the user to enter new hour and minute for task
    Parameters: None
    Return: time - string
    """
    print("Enter due time for your task.")
    hour_int = check_input.get_int_range(("Enter hour: "), 0, 23)
    minute_int = check_input.get_int_range(("Enter minute: "), 0, 59)

    hour = str(hour_int)
    minute = str(minute_int)

    if hour_int < 10:
        hour = "0" + str(hour)
    if minute_int < 10:
        minute = "0" + str(minute)
    
    return f"{hour}:{minute}"

def main():
    def display_current_task(choice, tasklist):
        """
        Description: display the main menu and the number of task
        Parameters: None
        Return: choice - int
        """
        task_ = tasklist[0]
        print(f"{choice}: {task_}")

    while True:
        choice = main_menu()
        tasklist = read_file()
        if choice == 1: #display current task
            if len(tasklist) == 0:
                print("All tasks are completed.")
            else:
                display_current_task("Current task",tasklist)

        elif choice == 2: #mark current task done, display new current task
            if len(tasklist) != 0:
                display_current_task("Marking current task as complete",tasklist)
                tasklist.pop(0)
                if len(tasklist)!= 0:
                    display_current_task("New current task is",tasklist)
                write_file(tasklist)
            else:
                print("All tasks are completed.")

        elif choice == 3: #postpont current task (get new date and time)
            if len(tasklist) != 0:
                display_current_task("Postponing task", tasklist)
                desc = tasklist[0].desc
                new_date = get_date()
                new_time = get_time()
                tasklist.pop(0)
                tasklist.append(Task(desc, new_date, new_time))
                tasklist.sort()
                write_file(tasklist)
            else:
                print("All tasks are completed.")

        elif choice == 4: #add new task (desc, date and time)
            desc = input("Enter description for your task: ")
            date = get_date()
            time = get_time()
            new_task = Task(desc, date, time)
            tasklist.append(new_task)
            tasklist.sort()
            write_file(tasklist)

        elif choice == 5: #save and quit
            print("Saving and exiting.")
            write_file(tasklist)
            quit()
    
main()