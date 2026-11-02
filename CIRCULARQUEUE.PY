# Circular Queue Implementation using Array
# Operations: Enqueue, Dequeue, Peek, Display

MAX_SIZE = 5

queue = [None] * MAX_SIZE
front = -1
rear = -1

while True:

    print("\n----- CIRCULAR QUEUE -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Enqueue
    if choice == 1:

        # Check whether queue is full
        if (rear + 1) % MAX_SIZE == front:
            print("Queue Overflow! Circular Queue is full.")

        else:
            value = int(input("Enter element to enqueue: "))

            # First element
            if front == -1:
                front = 0
                rear = 0

            else:
                rear = (rear + 1) % MAX_SIZE

            queue[rear] = value

            print(value, "inserted into circular queue.")

    # Dequeue
    elif choice == 2:

        if front == -1:
            print("Queue Underflow! Circular Queue is empty.")

        else:
            value = queue[front]

            print(value, "deleted from circular queue.")

            # Only one element was present
            if front == rear:
                front = -1
                rear = -1

            else:
                front = (front + 1) % MAX_SIZE

    # Peek
    elif choice == 3:

        if front == -1:
            print("Queue is empty.")

        else:
            print("Front element:", queue[front])

    # Display
    elif choice == 4:

        if front == -1:
            print("Queue is empty.")

        else:
            print("Circular Queue elements:", end=" ")

            i = front

            while True:
                print(queue[i], end=" ")

                if i == rear:
                    break

                i = (i + 1) % MAX_SIZE

            print()

    # Exit
    elif choice == 5:
        print("Program terminated.")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")
