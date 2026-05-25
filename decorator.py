# apply bottom to top
import functools
import time

def changeCase(func):
    def inner_fn():
        return func().upper()
    return inner_fn

@changeCase
def toUpperCase():
    return "hello"

# print(toUpperCase())


# with argument
def changeCaseWithArg(func):
    def inner_fn(x):
        return func(x).upper()
    return inner_fn

@changeCaseWithArg
def myFunction(nam):
    return "Hello " + nam

# print(myFunction('anurag'))

# with multiple args
def changeCaseWithMutipleArgs(func):
    def inner_fn(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner_fn

@changeCaseWithMutipleArgs
def myFunctionMultipleArgs(name, lastName):
    return "Hello " + name + " " + lastName

# print(myFunctionMultipleArgs("anurag", "dubey"))


# timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end =  time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def fetch_user():
    time.sleep(1)
    return [1,2,3,4]

# fetch_user()  

# cache deorator
def cache(func):
    store = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in store:
            print(f"Computing {func.__name__} {args}...")
            store[args] = func(*args)
        else:
            print(f"cached hit for {args}")
        return store[args]
    return wrapper

@cache
def get_user_from_db(user_id):
    return {"id": user_id, "name": "Alice"}

# get_user_from_db(1)   # Computing...
# get_user_from_db(1)   # Cache hit!
# get_user_from_db(2)   # Computing...
# get_user_from_db(2)   # Cache hit!
# get_user_from_db(1)   # Cache hit!


# Implement a decorator that retries a function up to 3 times on failure with exponential backoff.

def retry(max_retries = 3, initial_delay = 1, backoff_factor=2):
    def decorator(func):
        max = 3
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        print(f"Final attempt {attempt} failed. Giving up.") 
                        raise e
                    
                    print(f"Attempt {attempt} failed {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= backoff_factor


        return wrapper
    return decorator

attempts = 0

@retry(max_retries=3, initial_delay=1, backoff_factor=2)
def fetch_data():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ConnectionError("Network timeout!")
    return "Success! Data fetched."

# Run the decorated function
print(fetch_data())