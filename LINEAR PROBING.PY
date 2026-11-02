# Linear Probing

size = 10

hash_table = [-1] * size

def insert(key):
    index = key % size

    while hash_table[index] != -1:
        index = (index + 1) % size

    hash_table[index] = key

def display():
    for i in range(size):
        print(i, ":", hash_table[i])

# Main program

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

print("\nHash Table:")

display()
