stack=[]
queue=[]

def stack_insert():
    element = input("Enter an element to push to the stack: ")
    stack.append(element)
    print(f"Element {element} pushed to the stack.")

def stack_delete():
    if not stack:
        print("stack is empty")
    else:
        element = stack.pop()
        print(f"Element {element} popped from the stack.")


def stack_display():
    if not stack:
        print("stack is empty")
    else:
        print("stack elements:")
        for element in stack:
            print(element)

def queue_insert():
    element = input("Enter an element to queue: ")
    queue.append(element)
    print(f"Element {element} queue.")

def queue_delete():
    if not queue:
                print("Queue is empty.")
    else:
        element = queue.pop(0)
        print(f"Element {element} dequeued.")

def queue_display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue elements:")
        for element in queue:
            print(element)



while True:
        
        print("\nData Structure Operations:")
        print("1. Stack Operations")
        print("2. Queue Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                print("op")
                print("1. Insert into stack")
                print("2. Delete from stack")
                print("3. Display stack element")
                print("4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    stack_insert()
                elif choice == '2':
                    stack_delete()
                elif choice == '3':
                    stack_display()
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                print("op")
                print("1. Insert into queue")
                print("2. Delete from queue")
                print("3. Display queue element")
                print("4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    queue_insert()
                elif choice == '2':
                    queue_delete()
                elif choice == '3':
                    queue_display()
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
