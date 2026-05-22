# method A
import string_helpers

print(string_helpers.clean_text("   hello world   "))
print(string_helpers.reverse_text("hello world"))


# method B
from string_helpers import clean_text, reverse_text

print(clean_text("   anurag dubey   "))
print(reverse_text("anurag dubey"))


#method C
import string_helpers as sh

print(sh.clean_text("   python learning   "))
print(sh.reverse_text("python learning"))



