#Cecil Ryan
#1/18/24
#To-Do List

#Initialize
list = ["clean room", " homework", " wash dishes", " laundrey", " make dinner"]

#Functions
def add():
    task = input("What do you want to add to your list? ")
    position = int(input("Where would you like to add to your list? "))
    position = position - 1
    list.insert(position, task)
    print("Task added!")
    ToDo()
def view():
    print(list)
    ToDo()
def complete():
    position = int(input("What number item have you completed? "))
    task = input("What task have you comlpleted? ")
    position = position - 1
    list.pop(position)
    list.insert(position, " [x] " + task)
    print("Task marked as complete!")
    ToDo()
def remove():
    position = int(input("Where would you like to remove from your list? "))
    list.pop(position)
    print("Task removed!")
    ToDo()

def exit():
    print("Shutting down, have a good day.")
def ToDo():
    print("Welcome to your daily To-Do list!")
    print("\n 1. Add to list \n 2. View list \n 3. Mark task as completed \n 4. Remove from list \n 5. Exit")
    choice = int(input("Please choose what you would like to do!: "))
    if choice==1:
        add()
    if choice==2:
          view()
    if choice==3:
          complete()
    if choice==4:
          remove()
    if choice == 5:
         exit()

#Main
ToDo()