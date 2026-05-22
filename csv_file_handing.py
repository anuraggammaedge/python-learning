import csv

# with open('data.csv', 'r', newline='', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # for row in csv_reader:
#     #     print(row)

#     # for index, row in enumerate(csv_reader):
#     #     if index == 0:
#     #         print("Header:", row)
#     #     else:
#     #         print("Row:", row)

#     # for row in csv_reader:
#     #     print(row[0], row[1])

# with open("data.csv", "r", newline="", encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     list_of_dicts = []
#     for row in csv_reader:
#         list_of_dicts.append(row)
#         # print(row['ID'], row['FirstName'], row['Status'])

#     # print(list_of_dicts)

# new_users = {'ID': '10053', 'FirstName': 'Anurag', 'LastName': 'Dubey', 'Email': 'ivy.anurag@example.com', 'JoinDate': '2023-10-01', 'Score': '100', 'Status': 'Active'}
# duplicate_found = False
# with open("data.csv", "r", newline="", encoding='utf-8') as csv_file:
#     reader = csv.DictReader(csv_file)
    
#     for row in reader:
#          if row["ID"] == new_users["ID"]:
#             duplicate_id = row["ID"]
#             duplicate_found = True
#             print(f"Duplicate ID found: {duplicate_id}")
#             break
    
# if not duplicate_found:
#     with open("data.csv", "a", newline="", encoding='utf-8') as csv_file:
#         fieldnames = ['ID', 'FirstName', 'LastName', 'Email', 'JoinDate', 'Score', 'Status']
#         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         csv_writer.writerow(new_users)
#         print("New user added successfully.")
# else:
#     print("Duplicate ID found. New user not added.")


user_data = [
    {"ID": 101, "Name": "Alice Smith", "Email": "alice.smith@example.com", "JoinDate": "2025-03-15", "Score": 84.5, "Status": "Active"},
    {"ID": 102, "Name": "Bob Johnson", "Email": "bob.j@example.net", "JoinDate": "2024-11-02", "Score": 91.2, "Status": "Inactive"},
    {"ID": 103, "Name": "Charlie Brown", "Email": "charlie.b@example.org", "JoinDate": "2026-01-20", "Score": 73.0, "Status": "Active"},
    {"ID": 104, "Name": "Diana Prince", "Email": "diana@example.com", "JoinDate": "2025-05-12", "Score": 95.8, "Status": "Active"},
    {"ID": 105, "Name": "Evan Wright", "Email": "evan.w@example.net", "JoinDate": "2023-08-19", "Score": 62.1, "Status": "Suspended"}
]

def write_dict_to_csv(data, filename):
    if not data:
        print("No data to write.")
        return
    
    header = list(data[0].keys())

    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data written to {filename} successfully.")

write_dict_to_csv(user_data, "output.csv")