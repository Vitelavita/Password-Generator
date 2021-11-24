import random
import string

all= string.ascii_letters + string.digits + string.punctuation
print(all)
print("WELCOME TO PASSWORD GENERATOR 1.0")
x = input('Enter password length:')
try:
    x=int(x)
except:
    print("Not a valid number")
    x = int(input('Enter password length\n 0-93:'))

while x > 93:
    x = int(input('Enter password length\n 0-93:')) 
    if x<=93:
        break

length= x
passwd =  ''.join((random.choice(all)) for x in range(length))  

print("Your new password is...\n"+ passwd)  


