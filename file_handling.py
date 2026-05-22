file = open("data.txt", "r")

content = file.read()

if content:
    print(content)
else:
    print("File is empty")

# open('data.txt', 'w')  # delete data in file

file.close()

data = """ID,Name,Email,JoinDate,Score,Status
101,Alice Smith,alice.smith@example.com,2025-03-15,84.5,Active
102,Bob Johnson,bob.j@example.net,2024-11-02,91.2,Inactive
103,Charlie Brown,charlie.b@example.org,2026-01-20,73.0,Active
104,Diana Prince,diana@example.com,2025-05-12,95.8,Active
105,Evan Wright,evan.w@example.net,2023-08-19,62.1,Suspended
106,Fiona Gallagher,fiona@example.com,2025-12-01,88.4,Active
107,George Costanza,george@example.org,2024-04-30,55.0,Inactive
108,Hannah Abbott,hannah.a@example.net,2026-02-14,79.3,Active
"""

with open("data.txt", 'w') as file:
    file.write(data)
    print("Data written to file successfully.")


with open("data.txt", 'r') as file:
    first = file.readline()
    second = file.readline()

# print("First Line:", first.strip())
# print("Second Line:", second.strip())


lines_to_write = ["First line\n", "Second line\n", "Third line\n"]

with open("data.txt", 'a') as file:
    file.writelines(lines_to_write)
    print("Lines written to file successfully.")


file = open("data.txt")
lines = file.readlines()
# print("Lines read from file:", lines)

with open("data.txt", 'r') as file:
    for line in file:
        line.strip()
        # print(line.strip())


# Read exactly the first 2 lines of a file safely

with open("data.txt", 'r') as file:
    first_two_lines = [file.readline() for _ in range(4)]
    # print(first_two_lines)


# With tell() method we can get the current position of the file pointer. With seek() method we can change the position of the file pointer.

with open("data.txt", 'r+', encoding='utf-8') as file:
    print(file.tell())
    file.read(3)
    if file.tell() == 3:
        print("File pointer is at the correct position after reading 3 characters.")
    print(file.tell())

