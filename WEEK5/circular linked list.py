# Circular Linked List
# CSE25106

print("Implementation of CLL")


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Creation
    def create(self):
        n = int(input("Enter no of elements: "))

        for i in range(n):
            data = int(input("Enter the value: "))
            new = Node(data)

            if self.head is None:
                self.head = new
                new.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new
                new.next = self.head

    # Insert at Beginning
    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new.next = self.head
            self.head = new
            temp.next = self.head

    # Insert at End
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new
            new.next = self.head

    # Insert at Specific Index
    def insert_index(self, index, data):

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid index")
            return

        temp = self.head

        for i in range(index - 1):
            if temp.next == self.head:
                print("Invalid index")
                return

            temp = temp.next

        new = Node(data)
        new.next = temp.next
        temp.next = new

    # Delete Specific Value
    def delete(self, data):

        if self.head is None:
            print("No data")
            return

        # If head contains the value
        if self.head.data == data:

            # Only one node
            if self.head.next == self.head:
                self.head = None
                print("Value deleted")
                return

            # More than one node
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next

            print("Value deleted")
            return

        # Search for the value
        temp = self.head

        while temp.next != self.head and temp.next.data != data:
            temp = temp.next

        if temp.next == self.head:
            print("Value not present")
        else:
            temp.next = temp.next.next
            print("Value deleted")

    # Delete Beginning
    def delete_begin(self):

        if self.head is None:
            print("No data to delete")
            return

        # Only one node
        if self.head.next == self.head:
            print("Deleted value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        print("Deleted value =", self.head.data)

        temp.next = self.head.next
        self.head = self.head.next

    # Delete End
    def delete_end(self):

        if self.head is None:
            print("No data to delete")
            return

        # Only one node
        if self.head.next == self.head:
            print("Deleted value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        print("Deleted value =", temp.next.data)

        temp.next = self.head

    # Count Nodes
    def count(self):

        if self.head is None:
            print("No data to count")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes =", count)

    # Display / Traverse
    def display(self):

        if self.head is None:
            print("No data")
            return

        temp = self.head

        while True:
            print(temp.data, end=" --> ")
            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")


# Main Program
CLL = CircularLinkedList()

while True:

    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create CLL")
    print("2. Insert at beginning")
    print("3. Insert at ending")
    print("4. Insert at index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count no. of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        CLL.create()
        print("CLL is created")

    elif choice == 2:
        data = int(input("Enter data to insert: "))
        CLL.insert_begin(data)
        print("Data is inserted at beginning")

    elif choice == 3:
        data = int(input("Enter data to insert: "))
        CLL.insert_end(data)
        print("Data is inserted at ending")

    elif choice == 4:
        data = int(input("Enter data to insert: "))
        index = int(input("Enter the index: "))
        CLL.insert_index(index, data)

    elif choice == 5:
        data = int(input("Enter data to delete: "))
        CLL.delete(data)

    elif choice == 6:
        CLL.delete_begin()

    elif choice == 7:
        CLL.delete_end()

    elif choice == 8:
        CLL.count()

    elif choice == 9:
        CLL.display()

    elif choice == 10:
        print("Exiting the program")
        break

    else:
        print("Invalid choice")
