MAX = 5 
queue = [0] * MAX
front = -1 
rear = -1

def enqueue():
    global front,rear

    if rear==MAX -1:
        print("Queue overflow! Queue is full")
        return 
    value = int(input("Enter element to insert: "))

    if front == -1:
       front==0 
    rear +=1
    queue[rear] = value

    print("elemenet inserted succesfully")

def dequeue():
    global front, rear

    if front == -1 or front>rear:
        print(" Queue underflow! Queue is empty.")
        front = -1 
        rear =-1
        return 
    print(queue[front],"deleted succesfully.")

    front += 1 

    if front> rear:
        front=-1
        rear=-1

def display():
    if front==-1:
        print("Queue is Empty.")
        return

    print("Queue Elements: ")
    for i in range(front,rear+1):
        print(queue[i], end=" ")
    print()

while True:
    print("\n-----QUEUE MENU-----")
    print("1.Enqueu")
    print("2.dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter your choice: "))

    if choice ==1:
        enqueue()

    elif choice ==2:
        dequeue()

    elif choice==3:
        display()

    elif choice ==4:
        print("Program Ended.")
        break

    else:
        print(" Invalid Choice!")

