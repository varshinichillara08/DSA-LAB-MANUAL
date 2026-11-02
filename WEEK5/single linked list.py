# Singly Linked List
# CSE25106

print("Implementation of SLL")


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List Class
class SingleLinkedList:
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
            else:
                temp = self.head

                while temp.next:
                    temp = temp.next

                temp.next = new

    # Insert at Beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # Insert at End
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new

    # Insert at Specific Index
    def insert_index(self, index, data):

        if index == 0:
            self.insert_begin(data)
            return

        elif index < 0:
            print("Invalid index")
            return

        else:
            new = Node(data)
            temp = self.head

            for i in range(index - 1):
                if temp is None or temp.next is None:
                    print("Invalid index")
                    return

                temp = temp.next

            new.next = temp.next
            temp.next = new

    # Delete Specific Value
    def delete(self, data):

        if self.head is None:
            print("No data")
            return

        temp = self.head

        # If first node contains the value
        if temp.data == data:
            self.head = temp.next
            print("Value deleted")
            return

        # Search for the value
        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next is None:
            print("Value not present")
        else:
            temp.next = temp.next.next
            print("Value deleted")

    # Delete Beginning
    def delete_begin(self):

        if self.head is None:
            print("No data to delete")
        else:
            temp = self.head
            self.head = temp.next
            print("Deleted value =", temp.data)

    # Delete End
    def delete_end(self):

        if self.head is None:
            print("No data to delete")

        elif self.head.next is None:
            print("Deleted value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            print("Deleted value =", temp.next.data)
            temp.next = None

    # Count Nodes
    def count(self):

        if self.head is None:
            print("No data to count")
        else:
            count = 0
            temp = self.head

            while temp:
                count += 1
                temp = temp.next

            print(f"Number of nodes = {count}")

    # Display / Traverse
    def display(self):

        if self.head is None:
            print("No data")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" --> ")
                temp = temp.next

            print("None")


# Main Program
SLL = SingleLinkedList()

while True:

    print("\n----- SINGLY LINKED LIST -----")
    print("1. Create SLL")
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
        SLL.create()
        print("SLL is created")

    elif choice == 2:
        data = int(input("Enter data to insert: "))
        SLL.insert_begin(data)
        print("Data is inserted at beginning")

    elif choice == 3:
        data = int(input("Enter data to insert: "))
        SLL.insert_end(data)
        print("Data is inserted at ending")

    elif choice == 4:
        data = int(input("Enter data to insert: "))
        index = int(input("Enter the index: "))
        SLL.insert_index(index, data)

    elif choice == 5:
        data = int(input("Enter data to delete: "))
        SLL.delete(data)

    elif choice == 6:
        SLL.delete_begin()

    elif choice == 7:
        SLL.delete_end()

    elif choice == 8:
        SLL.count()

    elif choice == 9:
        SLL.display()

    elif choice == 10:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice")
