import random
import string

def generate_password(length):
    if length < 8: 
        print("Password length should be at least 8 characters for better security.")
        return None
    
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    result = ''.join(random.choice(pool) for _ in range(length))
    return result

password_length = 12
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
