import random
lower    = "abcdefghijklmnopqrstuvwxyz"
upper    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers  = "1234567890"
symbols  = "!@#$%^&*"
all      = lower+upper+numbers+symbols
length   = int(input("Enter length of the password:"))
password = "".join(random.sample(all,length))
print("Your generated password is=",password)
