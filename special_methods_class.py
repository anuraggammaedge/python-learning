#  With is keywors and works with context managers. 
#  it is synathic sugar of safer try/finally.

# Context manager is an object that managers:
#  1. setup of a resources.
#  2. cleanup of a resources.

# Acquire resource -> use resouce -> release resource

# __enter__ and __exit__ mehtod helps to manage custom context.
# Context manager guarantees cleanup.
# Commonly use with -> file handing, db connections, sockets, transactions, tempory files. 


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee: {self.name} | Salary: {self.salary}'
    
    def __repr__(self):
        return (
            f"Employee(emp_id={self.emp_id})"
            f"name='{self.name}', "
            f"salary={self.salary})"
        )
    
emp = Employee(1,'Anurag dubey', 30000000)
print(str(emp))
print(repr(emp))



class DatabaseConnection:
    def __init__(self, host, user, password ):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    # Acquire resource
    # Automatically called when entering `with` block
    def __enter__(self):
        print("Connecting to Database...")
        self.connection = "Database Connection Object"
        return self.connection
    
    # Cleanup resource
    # Automatically called when exiting `with` block
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing Database Connection...")

        self.connection = None

        if(exc_type):
            print(f"Exception occured: {exc_value}")

        print(traceback)

        return False

with DatabaseConnection(
    "localhost",
    "admin",
    "123"
) as db:
    print("executing database queries...")
    # print(10/0)
