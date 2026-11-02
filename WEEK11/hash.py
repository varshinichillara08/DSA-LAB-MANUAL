# Separate Chaining

size = 10

hash_table = [[] for i in range(size)]

def insert(key):
    index = key % size
    hash_table[index].append(key)

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
