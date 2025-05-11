#Random Password Generator
import random
import string

values = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
pass_length = 8
random_pass = ""
for i in range(pass_length):
  random_pass += random.choice(values)
print("These are some suggested passwords : ",random_pass)