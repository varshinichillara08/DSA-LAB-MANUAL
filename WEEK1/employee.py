def search(lst, key, index):
    if index >= len(lst):
        return False

    if lst[index] == key:
        return True

    return search(lst, key, index + 1)


employees = [101, 102, 103, 104, 105]

key = int(input("Enter Employee ID to search: "))

if search(employees, key, 0):
    print(f"Employee ID found: {key}")
else:
    print("Employee ID Not Found")
