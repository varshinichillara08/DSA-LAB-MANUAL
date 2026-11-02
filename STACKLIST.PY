# Stack using Linked List
# CSE25106


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack Class
class Stack:
    def __init__(self):
        self.top = None

    # Push Operation
    def push(self, item):
        new = Node(item)
        new.next = self.top
        self.top = new

        print(item, "pushed into the stack")

    # Pop Operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            self.top = self.top.next

            print(temp.data, "popped from the stack")

    # Peek Operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display Operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("The elements of the stack:")

            temp = self.top

            while temp is not None:
                print(temp.data)
                temp = temp.next


# Main Program

s = Stack()

while True:

    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to push: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
