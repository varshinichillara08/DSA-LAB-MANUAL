# Circular Queue using Singly Linked List
# Operations: Enqueue, Dequeue, Peek, Display


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        # Queue is empty
        if self.rear is None:
            self.rear = new_node
            self.rear.next = self.rear

        else:
            # New node is inserted after rear
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into circular queue.")

    # Dequeue operation
    def dequeue(self):
        if self.rear is None:
            print("Queue Underflow! Queue is empty.")
            return

        # Front node
        front = self.rear.next

        # Only one node
        if self.rear == front:
            self.rear = None

        else:
            self.rear.next = front.next

        print(front.data, "deleted from circular queue.")

    # Peek operation
    def peek(self):
        if self.rear is None:
            print("Queue is empty.")

        else:
            print("Front element:", self.rear.next.data)

    # Display operation
    def display(self):
        if self.rear is None:
            print("Queue is empty.")
            return

        front = self.rear.next
        current = front

        print("Circular Queue elements:", end=" ")

        while True:
            print(current.data, end=" ")
            current = current.next

            if current == front:
                break

        print()


# Create circular queue
queue = CircularQueue()


# Menu-driven program
while True:

    print("\n----- CIRCULAR QUEUE USING SINGLY LINKED LIST -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element to enqueue: "))
        queue.enqueue(value)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")
