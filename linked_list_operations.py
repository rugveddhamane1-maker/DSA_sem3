# ----------------------------
# Step 1 : Create Node Class
# ----------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ----------------------------
# Step 2 : Linked List Class
# ----------------------------

class LinkedList:

    def __init__(self):
        self.head = None

    # ----------------------------
    # Create List
    # ----------------------------
    def create_list(self):
        n = int(input("Enter number of nodes: "))

        if n <= 0:
            print("Invalid number of nodes.")
            return

        for i in range(n):
            value = int(input(f"Enter value {i+1}: "))
            self.insert_end(value)

        print("Linked List Created Successfully.")

    # ----------------------------
    # Insert Node at End
    # ----------------------------
    def insert_end(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # ----------------------------
    # Delete Node
    # ----------------------------
    def delete_node(self, value):

        if self.head is None:
            print("List is Empty.")
            return

        # Delete first node
        if self.head.data == value:
            self.head = self.head.next
            print("Node Deleted.")
            return

        previous = None
        temp = self.head

        while temp is not None and temp.data != value:
            previous = temp
            temp = temp.next

        if temp is None:
            print("Value Not Found.")
            return

        previous.next = temp.next
        print("Node Deleted Successfully.")

    # ----------------------------
    # Display List
    # ----------------------------
    def display(self):

        if self.head is None:
            print("Linked List is Empty.")
            return

        temp = self.head

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# ----------------------------
# Main Program
# ----------------------------

ll = LinkedList()

while True:

    print("\n====== LINKED LIST MENU ======")
    print("1. Create List")
    print("2. Insert Node")
    print("3. Delete Node")
    print("4. Display List")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        ll.create_list()

    elif choice == 2:
        value = int(input("Enter value to insert: "))
        ll.insert_end(value)
        print("Node Inserted.")

    elif choice == 3:
        value = int(input("Enter value to delete: "))
        ll.delete_node(value)

    elif choice == 4:
        ll.display()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")