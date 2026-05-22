# string_helpers.py

def clean_text(text):
    """Removes trailing spaces and capitalises text."""
    return text.strip().capitalize()

def reverse_text(text):
    """Reverses characters in a string."""
    return text[::-1]

print("String Helpers Module Loaded Successfully.")
print(reverse_text("from inside the module"))

# Prevent Code from Auto-Running on Import
if __name__ == '__main__':
    print("Running string_helpers.py directly.")
    print(clean_text("   hello world   "))