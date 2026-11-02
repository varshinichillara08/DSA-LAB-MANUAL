# Quadratic Probing

size = 10

hash_table = [-1] * size

def insert(key):
    index = key % size

    i = 0

    while i < size:
        new_index = (index + i * i) % size

        if hash_table[new_index] == -1:
            hash_table[new_index] = key
            return

        i += 1

    print("Hash Table is Full. Cannot insert", key)

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
