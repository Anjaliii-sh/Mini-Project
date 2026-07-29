#Mini Project 2
#Random password generator
import random
import string

char_values = string.ascii_letters + string.digits + string.punctuation
pass_len = 18

# password = ""
# for i in range(pass_len) :
#     password += random.choice(char_values)

# print("Your random password is : ",password)

# by list comprehension
password = "".join([random.choice(char_values) for i in range(pass_len)])
print("Your random password is : ",password)
